/*
test on Google API
*/
//var request = "https://www.googleapis.com/customsearch/v1?key=AIzaSyCTO7cWCMZDi-d7zMwqPEHLTDc5fUoa4vc&cx=012341178072093258148:lummcqp_ilw&q=hello";

var url = "https://www.googleapis.com/customsearch/v1?";
var apikey = "INPUT YOUR OWN KEY";  //register API key here: https://developers.google.com/custom-search/json-api/v1/overview
var engineID = "INPUT YOUR OWN"; //https://cse.google.com/all  | create search engine, then get the searchengine ID - make sure image is on
var query = "bowtie";  //search keywords
var request; //full API
var img;



function setup() {
	createCanvas(700,700);
	frameRate(1);
}

function gotData(data) {   //a callback needs an argument
	//console.log(data);  //to test if there is any response
	//freq = data.items[3].pagemap.cse_image[0].src;  //items responsible for which image
	freq = data.items[0].pagemap.cse_thumbnail[0].src;  // this is the thumbnail	
	console.log(freq);
	img = createImg(freq);
	img.position(0,0);
	
}

function draw() {
		request = url + "key=" + apikey + "&cx=" + engineID + "&q=" + query;
		console.log(request);
		loadJSON(request, gotData); //this is the key syntax and line of code to make a query request and get a query response
		noLoop();
}

