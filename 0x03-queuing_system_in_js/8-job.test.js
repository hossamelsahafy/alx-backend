import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

// Create a queue
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function () {
  // Clear the queue before each test
  beforeEach(done => {
    kue.Job.rangeByState('queued', 0, -1, 'asc', (err, jobs) => {
      if (err) return done(err);
  
      // Remove each job in the queue
      const deleteJobs = jobs.map(job => new Promise((resolve, reject) => {
        job.remove(err => {
          if (err) return reject(err);
          resolve();
        });
      }));
  
      Promise.all(deleteJobs).then(() => done()).catch(done);
    });
  });
  

  // Exit test mode after each test
  afterEach(done => {
    done();
  });

  it('should display an error message if jobs is not an array', function () {
    const invalidJobs = {};
    expect(() => createPushNotificationsJobs(invalidJobs, queue))
      .to.throw('Jobs is not an array');
  });

  it('should create two new jobs in the queue', function (done) {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234' },
      { phoneNumber: '4153518790', message: 'This is the code 5678' }
    ];
  
    createPushNotificationsJobs(jobs, queue);
  
    // Add a short delay to ensure jobs are processed
    setTimeout(() => {
      // Check the number of jobs before the test
      kue.Job.rangeByState('queued', 0, -1, 'asc', (err, jobsBefore) => {
        if (err) return done(err);
  
        console.log('Jobs before test:', jobsBefore.length);
  
        // Retrieve jobs to validate
        kue.Job.rangeByState('queued', 0, -1, 'asc', (err, jobs) => {
          if (err) return done(err);
  
          console.log('Retrieved jobs:', jobs.length); // Log number of jobs for debugging
  
          expect(jobs).to.have.lengthOf(2);
          expect(jobs[0].type).to.equal('push_notification_code_3');
          expect(jobs[1].type).to.equal('push_notification_code_3');
          
          done();
        });
      });
    }, 500); // Increase delay if needed
  });
  
});
