import kue from 'kue';
import redis from 'redis';

const redisClient = redis.createClient();
const queue = kue.createQueue({ redis: redisClient });

const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a test notification',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (err) {
      console.error(`Error creating job: ${err.message}`);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
});
