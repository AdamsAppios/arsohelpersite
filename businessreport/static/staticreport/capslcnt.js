function readOutLoud(message) {
  var speech = new SpeechSynthesisUtterance();

  // Set the text and voice attributes.
  var isSafari =
    navigator.vendor &&
    navigator.vendor.indexOf("Apple") > -1 &&
    navigator.userAgent &&
    navigator.userAgent.indexOf("CriOS") == -1 &&
    navigator.userAgent.indexOf("FxiOS") == -1;
  rate = isSafari ? 1.5 : 2.4;
  var voices = window.speechSynthesis.getVoices();
  speech.voice = isSafari ? voices[11] : voices[1];
  speech.text = message;
  speech.volume = 1;
  speech.rate = rate;
  speech.pitch = 1;
  window.speechSynthesis.cancel();
  window.speechSynthesis.speak(speech);
}
var bills = ["5", "10", "20", "25", "50", "100", "500", "1000"],
  defaultMultiple = 1;
srate = 1.9;
voice = "US English Male";
defaultMultiple = 1;
$("#multiple").val(bills[defaultMultiple]);
$("#largestbuttonever").on('click', function(e) {
  $("#largestbuttonever").css("background-color", "white");
  if ($("#multiple").val() == "") $("#multiple").val(bills[defaultMultiple]);
  $("#totalCount").val(
    (
      parseInt($("#totalCount").val()) +
      1 * parseInt($("#multiple").val())
    ).toString()
  );
  $("#largestbuttonever").text($("#totalCount").val());
  var $el = $("#largestbuttonever"),
    x = 110,
    originalColor = $el.css("background-color");
  $el.css("background-color", "red");
  setTimeout(function () {
    $el.css("background-color", originalColor);
  }, x);
  readOutLoud($("#totalCount").val());
  $("#multiple").val(bills[defaultMultiple]);
});

$("#multiple").focus(function () {
  var field = $(this);
  if (field.val() != "") {
    field.val("");
  }
});

$("#multiple").on("blur", function () {
  if ($(this).val().trim().length == 0) {
    $(this).val("10");
  }
});

$("#left").click(function () {
  if (defaultMultiple == 0) {
    defaultMultiple = bills.length - 1;
    $("#multiple").val(bills[defaultMultiple]);
  } else $("#multiple").val(bills[--defaultMultiple]);
});

$("#right").click(function () {
  if (defaultMultiple == bills.length - 1) {
    $("#multiple").val(bills[(defaultMultiple = 0)]);
  } else $("#multiple").val(bills[++defaultMultiple]);
});

$("#clearCnt").click(function () {
  $("#largestbuttonever").css("background-color", "white");
  $("#largestbuttonever").text("0");
  $("#totalCount").val(0);
});
