$(document).ready(function () {
  function ReportClass() {
    this.dealPrice = 10;
    this.pickPrice = 15;
    this.rndPrice = 150;
    this.radioValue = $("input[name='chooseradio']:checked").attr("id");
    this.radArray = [
      "deal",
      "pick",
      "rndRad",
      "smallRad",
      "squareRad",
      "dealCustRad",
      "suspect",
    ];
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
  ReportClass.prototype.ajaxLoadSave = function (option) {
    var crsf_value = document.querySelector("[name=csrfmiddlewaretoken]").value;
    data = {
      csrfmiddlewaretoken: crsf_value,
      option: option,
      location: $("#lugar option:selected").text(),
      date: $("#date").val(),
      timeCC: $("#timeCC").val(),
      dayparts: checkboxToString(),
      dealer: $("#dealer").val(),
      pickup: $("#pickup").val(),
      smallGal: $("#smallGal").val(),
      rnd: $("#rnd").val(),
      squareGal: $("#squareGal").val(),
      dealCust: $("#dealCust").val(),
      suspectText: $("#suspectText").val(),
    };
    if (option == "save") {
      $.ajax({
        url: "ajax/refillingloadsave/",
        data: data,
        method: "POST",
        dataType: "json",
        success: function (data) {},
      });
    } else if (option == "load") {
      $.ajax({
        url: "ajax/refillingloadsave/",
        data: data,
        method: "POST",
        dataType: "json",
        success: function (data) {
          $("#timeCC").val(data["timeCC"]);
          $("#dealer").val(data["dealer"]);
          $("#pickup").val(data["pickup"]);
          $("#rnd").val(data["rnd"]);
          $("#smallGal").val(data["smallGal"]);
          $("#squareGal").val(data["squareGal"]);
          $("#dealCust").val(data["dealCust"]);
          $("#suspectText").val(data["suspectText"]);
          arrDayParts = data["dayparts"].split(";");
          for (var i = 0; i < arrDayParts.length; i++) {
            $("input[type='checkbox'][value='" + arrDayParts[i] + "']").prop(
              "checked",
              true
            );
          }
        },
      });
    }
  };
  ReportClass.prototype.binop = function (a, b, op) {
    switch (op) {
      case "add":
        return a + b;
      case "sub":
        return a - b;
    }
  };
  ReportClass.prototype.buttonOperation = function (operation) {
    let radioValue = $("input[name='chooseradio']:checked").attr("id");
    let incrementVal = parseInt($("#incrementVal").val());
    messageop = operation == "add" ? "plus " : "minus ";
    switch (radioValue) {
      case "deal":
        dealer = parseInt($("#dealer").val());
        $("#dealer").val(this.binop(dealer, incrementVal, operation));
        messageop += " deal";
        break;
      case "pick":
        pickup = parseInt($("#pickup").val());
        $("#pickup").val(this.binop(pickup, incrementVal, operation));
        messageop += " pick";
        break;
      case "rndRad":
        rnd = parseInt($("#rnd").val());
        $("#rnd").val(this.binop(rnd, incrementVal, operation));
        messageop += " round";
        break;
      case "smallRad":
        smallGal = parseInt($("#smallGal").val());
        $("#smallGal").val(this.binop(smallGal, incrementVal, operation));
        messageop += " small";
        break;
      case "squareRad":
        squareGal = parseInt($("#squareGal").val());
        $("#squareGal").val(this.binop(squareGal, incrementVal, operation));
        messageop += " square";
        break;
      case "dealCustRad":
        dealCust = parseInt($("#dealCust").val());
        $("#dealCust").val(this.binop(dealCust, incrementVal, operation));
        messageop += " Customer";
        break;
      case "suspect":
        var asadapit = prompt("Where did it happen?");
        var timebeg = prompt("Time beg?");
        var timend = prompt("Beg:" + timebeg + ", Time end?");
        var textareaval = $("#suspectText").val();
        $("#suspectText").val(
          textareaval + timebeg + "-" + timend + "=" + asadapit + "\n"
        );
        messageop += " suspect";
        break;
    }
    this.readOutLoud(messageop);
    $("#incrementVal").val("1");
  };
  ReportClass.prototype.changeBGColor = function (colo) {
    var el = $("body"),
      x = 110,
      originalColor = "white";
    el.css("background", colo);
    setTimeout(function () {
      el.css("background", originalColor);
    }, x);
  };
  ReportClass.prototype.keyPress = function (event) {
    let radArray = this.radArray;
    let radioValue = $("input[name='chooseradio']:checked").attr("id");
    let indexRad = radArray.indexOf(radioValue);
    if (event.keyCode === 13) {
      $("#addBtn").click();
    } else if (event.keyCode === 109) {
      $("#subBtn").click();
    } else if (event.keyCode === 39) {
      indexRad++;
      if (indexRad > radArray.length - 1) {
        indexRad = 0;
      }
      $(`#${radArray[indexRad]}`).prop("checked", true);
    } else if (event.keyCode === 37) {
      indexRad--;
      if (indexRad < 0) {
        indexRad = radArray.length - 1;
      }
      $(`#${radArray[indexRad]}`).prop("checked", true);
    }
  };
  function checkboxToString() {
    arrCheck = [];
    $("form input[name=dayparts]").each(function (idx, elem) {
      var is_checked = $(this).prop("checked");
      // Do something with is_checked
      if (is_checked) arrCheck.push($(this).attr("id"));
    });
    return arrCheck.join(";");
  }

  var globalClass = new TmbReportClass();
  $("#saveBtn").click(function () {
    globalClass.ajaxLoadSave("save");
  });
  $("#loadBtn").click(function () {
    globalClass.ajaxLoadSave("load");
  });

  $("form input[type]").on("click focusin", function () {
    this.value = "";
  });
  $("form input[type=number]").on("blur", function () {
    if ($(this).val().trim().length == 0) {
      if ($(this).attr("name") == "incrementVal") $(this).val("1");
      else $(this).val("0");
    }
  });
  $("#lugar").change(function () {
    lugar = $("#lugar option:selected").text();
    switch (lugar) {
      case "Talamban":
        globalClass = new TmbReportClass();
        break;
      case "Labangon":
        globalClass = new LabReportClass();
        break;
      case "Kalimpyo":
        globalClass = new KalimpReportClass();
        break;
    }
  });

  $("#subBtn").click(function () {
    globalClass.buttonOperation("sub");
    globalClass.changeBGColor("red");
  });
  $("#addBtn").click(function () {
    globalClass.buttonOperation("add");
    globalClass.changeBGColor("blue");
  });

  $(document.body).keyup(function (event) {
    globalClass.keyPress(event);
  });
});
