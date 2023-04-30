/*
 Title: walker-assignment5.2.js
 Author: Megan Walker
 Date: 04/15/23
 Description: walker-assignment5.2.js
 References: WEB 335 GitHub, & WEB 335 Assign_5, provided by Professor Krasso
 */

//load user.js module
load("users.js");

// Write a query to add a new user to the users collection.
db.users.insertOne({
  firstName: "Emily",
  lastName: "Jones",
  employeeId: "1015",
  email: "ejones@gmail.com",
  dateCreated: ISODate("2023-04-15T00:00:00.0Z"),
});

//Write a query to update Mozart's email address to mozart@me.com
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

//Write a query to prove the email address was updated.
db.users.find({ lastName: "Mozart" });

//Write a query to list all documents in the user's collection. Use projections to only display the firstName, lastName, and email fields.
db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 });
