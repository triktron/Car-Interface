setInterval(function() {
  document.querySelector('.time').innerHTML = new Date().getHours() + ":" + (new Date().getMinutes() <= 9 ? "0" : "") + new Date().getMinutes();
}, 30000)

document.querySelector('.time').innerHTML = new Date().getHours() + ":" + (new Date().getMinutes() <= 9 ? "0" : "") + new Date().getMinutes();

console.log(process.versions);

var apps = document.querySelectorAll('.app a');
// document.querySelector("#appView").addEventListener("dom-ready", function(){ document.querySelector("#appView").openDevTools(); });
apps.forEach(function(app) {
  console.log(app);

  app.addEventListener("click", function(e) {
    e.preventDefault();

    console.log(app, e);
    var wbv = document.querySelector("#appView");
    if (wbv.src != app.href) wbv.loadURL(app.href);

    if (!wbv.isLoading()) {
      wbv.style["z-index"] = "1";
    } else {
      wbv.addEventListener("did-finish-load", function() {
        wbv.style["z-index"] = "1"
      }, {
        once: true
      })
    }

    document.querySelector('.backBTN').style.display = "block";
    document.querySelector('.spinner').style.display = "block";
  })
})

document.querySelector('.backBTN').addEventListener("click", function() {

  document.querySelector("#appView").style["z-index"] = "-1";
  document.querySelector('.backBTN').style.display = "none";
  document.querySelector('.spinner').style.display = "none";
})
