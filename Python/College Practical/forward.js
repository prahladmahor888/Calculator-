var nodemailer = require ("nodemailer");
var smtpTransport = nodemailer.createTransport ("SMTP", {
  host: '',
  port: 25
});

var maillist = [
  '****.sharma3@****.com',
  '****.bussa@****.com',
  '****.gawri@****.com',
  // add more email addresses here
];

var msg = {
  from: "******", // sender address
  subject: "Hello ✔", // Subject line
  text: "Hello This is an auto generated Email for testing from node please ignore it ✔", // plaintext body
  cc: "*******",
  to: maillist // array of recipients
}

smtpTransport.sendMail (msg, function (err) {
  if (err) {
    console.log ('Sending failed: ' + err);
    return;
  } else {
    console.log ('Sent successfully');
  }
});