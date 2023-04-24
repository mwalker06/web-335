/*
 Title: walker-assignment6.2.js
 Author: Megan Walker
 Date: 04/23/23
 Description: walker-assignment6.2.js
 References: WEB 335 GitHub, & WEB 335 Assign_6, provided by Professor Krasso
 */

//load houses.js module
load("houses.js");

//Write a query to show a list of documents in the houses collection
db.houses.find({});

//Write a query to show a list of documents in the student’s collection
db.students.find({});

//Write a query to add a document to the student’s collection
db.students.insertOne({
  firstName: "Megan",
  lastName: "Walker",
});

//Write a query to delete the document you created
db.students.deleteOne({
  firstName: "Megan",
  lastName: "Walker",
});

//Write a query to show a list of students by house.
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "studentsInHouse",
    },
    },
]);

//Write a query to show a list of students for house Gryffindor.
db.houses.aggregate([
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "studentsInHouse",
      },
    },
    {
      $match: {
        founder: "Godric Gryffindor",
      },
    },
  ]);

//Write a query to show a list of students for house Hufflepuff.
db.houses.aggregate([
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "studentsInHouse",
      },
    },
    {
      $match: {
        founder: /.*Hufflepuff.*/,
      },
    },
  ]);
  
