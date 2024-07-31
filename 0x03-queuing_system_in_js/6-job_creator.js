import kue from 'kue';

// Create a Kue queue with default Redis configuration
const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
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
