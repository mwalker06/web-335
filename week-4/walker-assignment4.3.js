/*
 Title: walker-assignment4.3.js
 Author: Megan Walker
 Date: 04/08/23
 Description: walker-assignment4.3.js
 References: WEB 335 GitHub, & WEB 335 Assign_4, provided by Professor Krasso
 */

// load user.js module
load("user.js");

// display all of the documents in the user’s collection
db.users.find({});

// find the user with an email address of jbach@me.com
db.users.find({ email: "jbach@me.com" });

//find a user with the last name of Mozart
db.users.find({ lastName: "Mozart" });

//find a user with a first name of Richard
db.users.find({ firstName: "Richard" });

//find a user with an employeeId of 1010
db.users.find({ employeeId: "1010" });
