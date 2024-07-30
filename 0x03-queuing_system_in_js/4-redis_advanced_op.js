const redis = require('redis')
const client = redis.createClient();
client.on('conect', () => {
    console.log("Redis client connected to the server")
});
client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`)
});
function createHash() {
    client.hset('HolbertonSchools', 'Portland', 50, redis.print)
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print)
    client.hset('HolbertonSchools', 'New York', 20, redis.print)
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print)
    client.hset('HolbertonSchools', 'Cali', 40, redis.print)
    client.hset('HolbertonSchools', 'Paris', 2, redis.print)
}
function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
        if(err) {
            console.log(`Error getting hash: ${err.message}`)
        } else {
            console.log(reply);
        }
    })
}
createHash();
displayHash();
