import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue({
    redis: {
      port: 6379,
      host: '127.0.0.1'
    }
  });

const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  }
];

createPushNotificationsJobs(list, queue);
