const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
  ];
  
  function getItemById(id) {
    return listProducts.find(product => product.id === id);
  }
  
  const express = require('express');
  const redis = require('redis');
  const { promisify } = require('util');
  
  const app = express();
  const port = 1245;
  
  // Connect to Redis
  const redisClient = redis.createClient();
  const reserveStock = promisify(redisClient.set).bind(redisClient);
  const getReservedStock = promisify(redisClient.get).bind(redisClient);
  
  // Error handling for Redis
  redisClient.on('error', (err) => {
    console.error(`Redis error: ${err}`);
  });
  
  // Middleware to set response type to JSON
  app.use((req, res, next) => {
    res.setHeader('Content-Type', 'application/json');
    next();
  });
  
  // Route to get all products
  app.get('/list_products', (req, res) => {
    const products = listProducts.map(({ id, name, price, stock }) => ({
      itemId: id,
      itemName: name,
      price,
      initialAvailableQuantity: stock
    }));
    res.json(products);
  });
  
  // Route to get product details
  app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);
  
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    try {
      const reservedStock = await getCurrentReservedStockById(itemId);
      const currentQuantity = product.stock - (reservedStock || 0);
  
      res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity
      });
    } catch (error) {
      res.status(500).json({ status: 'Error retrieving reserved stock' });
    }
  });
  
  // Route to reserve a product
  app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const product = getItemById(itemId);
  
    if (!product) {
      return res.json({ status: 'Product not found' });
    }
  
    try {
      const reservedStock = await getCurrentReservedStockById(itemId);
      const currentQuantity = product.stock - (reservedStock || 0);
  
      if (currentQuantity <= 0) {
        return res.json({ status: 'Not enough stock available', itemId });
      }
  
      await reserveStock(`item.${itemId}`, (reservedStock || 0) + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } catch (error) {
      res.status(500).json({ status: 'Error reserving product' });
    }
  });
  
  // Start the server
  app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
  });
  
  // Function to reserve stock by ID
  async function reserveStockById(itemId, stock) {
    await reserveStock(`item.${itemId}`, stock);
  }
  
  // Function to get current reserved stock by ID
  async function getCurrentReservedStockById(itemId) {
    try {
      const stock = await getReservedStock(`item.${itemId}`);
      return parseInt(stock, 10) || 0;
    } catch (error) {
      console.error(`Error retrieving reserved stock: ${error}`);
      return 0;
    }
  }
  