"use strict";

console.log("Hello world");

function User(name) {
    this.name = name;
}

User.prototype.hello = function (who) {
    console.log("Hi, " + who.name);
};

let mark = new User("Mark");
let david = new User("David");

mark.hello(david);

module.exports = User;
