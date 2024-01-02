// script.js
// get the canvas element and its context
var canvas = document.getElementById ("canvas");
var ctx = canvas.getContext ("2d");

// get the score element
var score = document.getElementById ("score");

// set the size of each cell
var cellSize = 10;

// set the initial position and direction of the snake
var snake = [{x: 200, y: 200}, {x: 190, y: 200}, {x: 180, y: 200}];
var direction = "right";

// set the initial position of the food
var food = {x: Math.floor (Math.random () * 40) * cellSize,
            y: Math.floor (Math.random () * 40) * cellSize};

// set the initial score
var scoreValue = 0;

// draw a cell on the canvas
function drawCell (x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect (x, y, cellSize, cellSize);
}

// draw the snake on the canvas
function drawSnake () {
  for (var i = 0; i < snake.length; i++) {
    drawCell (snake [i].x, snake [i].y, "green");
  }
}

// draw the food on the canvas
function drawFood () {
  drawCell (food.x, food.y, "red");
}

// update the position of the snake
function updateSnake () {
  // get the head of the snake
  var head = snake [0];
}
