import redis from 'redis';
import { promisify } from 'util';
const client = redis.createClient();

client.on('connect', () => {
 console.log("Redis client connected to the server")
})
client.on('error', (error) => {
  console.log("Redis client not connected to the server: ERROR_MESSAGE")
})

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
    try {
      await new Promise((resolve, reject) => {
        client.set(schoolName, value, (err, reply) => {
          if (err) {
            reject(err);
          } else {
            console.log(`Reply: ${reply}`);
            resolve(reply)
          }
        });
      });
    } catch (err) {
      console.log(`Error setting ${schoolName}: ${err.message}`);
    }
  }

async function displaySchoolValue(schoolName) {
    try {
      const value = await new Promise((resolve, reject) => {
        client.get(schoolName, (err, reply) => {
          if (err) {
            reject(err);
          } else {
            resolve(reply);
          }
        });
      });
      console.log(value);
    } catch (err) {
      console.log(`Error getting ${schoolName}: ${err.message}`);
    }
  }

(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
  client.quit();
})();
