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
  LabReportClass.prototype = Object.create(ReportClass.prototype);
  TmbReportClass.prototype = Object.create(ReportClass.prototype);
});
