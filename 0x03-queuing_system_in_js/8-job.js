import kue from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const jobInstance = queue.create('push_notification_code_3', job).save((err) => {
      if (err) {
        console.error('Error creating job:', err);
      } else {
        console.log('Notification job created:', jobInstance.id);
      }
    });

    jobInstance.on('complete', () => {
      console.log('Notification job', jobInstance.id, 'completed');
    });

    jobInstance.on('failed', (errorMessage) => {
      console.log('Notification job', jobInstance.id, 'failed:', errorMessage);
    });
  });
};

export default createPushNotificationsJobs;
