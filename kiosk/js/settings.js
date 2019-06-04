const execSync = require('child_process').exec


function setBrightness(level) {
  execSync('sudo bash -c "echo ' + level + ' > /sys/class/backlight/rpi_backlight/brightness"')
}

// new RangeSlider($(".brightness"), {
//     size: 1,
//     borderSize: 0.4,
//     percentage: 100,
//     pollLimit: 20,
//     onMove: function(b,a) { setBrightness(Math.max(10,Math.round(a * 2.25)))},
//     onDown: function(b,a) { setBrightness(Math.max(10,Math.round(a * 2.25)))}
// });

var ranger = document.querySelector(".range input")
var done = document.querySelector(".range .done")

var rect = ranger.getClientRects()[0]
done.style.width = rect.width * ranger.value / ranger.max - 6 + "px";
done.style.top = rect.top + 2 + "px";
done.style.left = rect.left + "px";

ranger.onchange = () => {
  done.style.width = rect.width * ranger.value / ranger.max - 6 + "px";
  setBrightness(Math.round(ranger.value * 2.4 + 10));
}
ranger.oninput = () => {
  done.style.width = rect.width * ranger.value / ranger.max - 6 + "px";
  setBrightness(Math.round(ranger.value * 2.4 + 10));
}


document.querySelector(".openDev").addEventListener("click", function() {

  require('remote').getCurrentWindow().toggleDevTools();
})



$('#reboot').confirmation({
  placement: "bottom",
  onConfirm: () => {
    execSync('sudo reboot')
  }
});

$('#shutdown').confirmation({
  placement: "bottom",
  onConfirm: () => {
    execSync('sudo shutdown now')
  }
});
