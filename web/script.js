// Create a variable for the canvas and it's context
var canvas = document.getElementById("pawnfork-canvas");
var ctx = canvas.getContext("2d");

// Initialise an image object
var image = new Image();

// When it loads an image
image.onload = function() {
  var canvasStyle = getComputedStyle(canvas);
  var canvasWidth = canvasStyle.width.replace("px", "");
  var imageRatio = this.width / this.height;
  var canvasHeight = canvasWidth / imageRatio;
  canvas.style.height = canvasHeight + "px";
  canvas.width = canvasWidth;
  canvas.height = canvasHeight;
  ctx.drawImage(this, 0, 0, canvasWidth, canvasHeight);
};

// Load an image
image.src = '../static/images/chessboard.png'