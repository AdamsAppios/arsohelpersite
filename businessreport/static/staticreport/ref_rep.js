$(document).read(function () {
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

  LabReportClass.prototype = Object.create(ReportClass.prototype);
  TmbReportClass.prototype = Object.create(ReportClass.prototype);
  KalimpReportClass.prototype = Object.create(ReportClass.prototype);
  LabReportClass.prototype.updateCTOCalc = function () {
    var ctoCalc =
      (parseInt($("#dealText").val()) - parseInt($("#less").val())) *
        this.dealPrice +
      parseInt($("#pickText").val()) * this.pickPrice +
      parseInt($("#goodlyText").val()) * this.goodlyPrice +
      parseInt($("#smallText").val()) * this.smallPrice +
      parseInt($("#squareText").val()) * this.squarePrice +
      parseInt($("#rndText").val()) * this.rndPrice -
      parseInt($("#totalExpenses").html()) -
      parseInt($("#cashTkn").val());
    $("#ctoCalc").val(ctoCalc);
  };
  TmbReportClass.prototype.updateCTOCalc = function () {
    var ctoCalc =
      parseInt($("#dealText").val()) * this.dealPrice +
      parseInt($("#pickText").val()) * this.pickPrice +
      parseInt($("#rndText").val()) * this.rndPrice -
      parseInt($("#totalExpenses").html()) -
      parseInt($("#cashTkn").val());
    $("#ctoCalc").val(ctoCalc);
  };
  KalimpReportClass.prototype.updateCTOCalc = function () {
    var ctoCalc =
      (parseInt($("#dealText").val()) - parseInt($("#less").val())) *
        this.dealPrice +
      parseInt($("#pickText").val()) * this.pickPrice +
      parseInt($("#smallSquare").val()) * this.smallSqPrice +
      parseInt($("#bakeryGal").val()) * this.bakeryPrice +
      parseInt($("#smallText").val()) * this.smallPrice +
      parseInt($("#squareText").val()) * this.squarePrice +
      parseInt($("#rndText").val()) * this.rndPrice -
      parseInt($("#totalExpenses").html()) -
      parseInt($("#cashTkn").val());
    $("#ctoCalc").val(ctoCalc);
  };
});
