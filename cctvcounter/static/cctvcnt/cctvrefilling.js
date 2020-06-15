$(document).ready(function () {
  function ReportClass() {
    this.dealPrice = 10;
    this.pickPrice = 15;
    this.rndPrice = 150;
  }
  function LabReportClass() {
    ReportClass.call(this);
    this.squarePrice = 15;
    this.smallPrice = 8;
    this.goodlyPrice = 8;
  }
  function TmbReportClass() {
    ReportClass.call(this);
    this.dealPrice = 8;
    this.pickPrice = 12;
  }
  function KalimpReportClass() {
    ReportClass.call(this);
    this.squarePrice = 15;
    this.smallPrice = 5;
    this.smallSqPrice = 10;
    this.bakeryPrice = 15;
  }
  function KalimpReportClass() {
    ReportClass.call(this);
    this.squarePrice = 15;
    this.smallPrice = 5;
    this.smallSqPrice = 10;
    this.bakeryPrice = 15;
  }
  function GoldswanReportClass() {
    ReportClass.call(this);
    this.squarePrice = 15;
    this.smallPrice = 5;
    this.smallSqPrice = 10;
    this.bakeryPrice = 15;
  }
  LabReportClass.prototype = Object.create(ReportClass.prototype);
  TmbReportClass.prototype = Object.create(ReportClass.prototype);
  KalimpReportClass.prototype = Object.create(ReportClass.prototype);
  ReportClass.prototype.readOutLoud = function (message) {
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
  };
  $("#saveBtn").click(function () {
    arrCheck = [];
    $("form input[name=dayparts]").each(function (idx, elem) {
      var is_checked = $(this).prop("checked");
      // Do something with is_checked
      if (is_checked) arrCheck.push($(this).val());
    });
    alert(arrCheck.join(";"));
  });

  $("form input[type]").on("click focusin", function () {
    this.value = "";
  });
  $("form input[type=number]").on("blur", function () {
    if ($(this).val().trim().length == 0) {
      $(this).val("0");
    }
    globalClass.updateCTOCalc();
  });
});
