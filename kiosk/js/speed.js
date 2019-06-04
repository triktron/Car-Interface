// var gauge = new RadialGauge({
//     renderTo: 'c',
//     width: 400,
//     height: 400,
//     units: "Km/h",
//     minValue: 0,
//     maxValue: 220,
//     majorTicks: [
//         "0",
//         "20",
//         "40",
//         "60",
//         "80",
//         "100",
//         "120",
//         "140",
//         "160",
//         "180",
//         "200",
//         "220"
//     ],
//     minorTicks: 2,
//     strokeTicks: true,
//     highlights: [
//         {
//             "from": 160,
//             "to": 220,
//             "color": "rgba(200, 50, 50, .75)"
//         }
//     ],
//     colorPlate: "#fff",
//     borderShadowWidth: 0,
//     borders: false,
//     needleType: "arrow",
//     needleWidth: 2,
//     needleCircleSize: 7,
//     needleCircleOuter: true,
//     needleCircleInner: false
// }).draw();

// websocket = new WebSocket("ws://localhost:8080/serial");//ws://10.0.4.80:8080/serial
//     websocket.onopen = function(evt) { onOpen(evt) };
//     websocket.onclose = function(evt) { onClose(evt) };
//     websocket.onmessage = function(evt) { onMessage(evt) };
//     websocket.onerror = function(evt) { onError(evt) };
//
//     function onOpen(evt)
//   {
//   }
//
//   function onClose(evt)
//   {
//
//   }
//   function onMessage(evt)
//   {
//     if (evt.data[0] == "S") {
//       document.querySelector(".speed").setAttribute('data-value', evt.data.slice(1));
//     }
//   }
//
//   function onError(evt)
//   {
//
//   }

const child_process = require('child_process');


const child = child_process.spawn('python3', ['-u', '/home/pi/interface/usb.py']);

var buffer = "";

child.stderr.on('data', function (data) {

});

child.stdout.on('data', function(data) {
  buffer = data.toString().split("\n");
  s = 0;

  for (var i of buffer) if (i[0] == "S"){
    var d = Number(i.slice(-1));

    if (d != NaN)  s = d;
  }

  var speed = 20 * (54/17) * (1/Math.PI*0.35) * 4 * 3.6;
  document.querySelector(".speed").setAttribute('data-value', s);
});

child.on('exit', function (code) {
  console.log('child process exited with code ' + code.toString());
});

function proccesBuffer() {

}

console.log("hy");
// var i = 0;
// setInterval(() => {
//  i+= 0.5;
//  if (i > 18) i = 0;
//  document.querySelector(".speed").setAttribute('data-value', i);
//
// }, 200)

var x = 100;
setInterval(() => {
 x-= 5;
 if (x <= 0) x = 100;
 document.querySelector(".batt").setAttribute('data-value', x);

}, 200)
