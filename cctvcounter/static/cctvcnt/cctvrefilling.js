function ReportClass() {
  this.dealPrice = 10;
  this.pickPrice = 15;
  this.rndPrice = 150;
}
function TmbReportClass() {
  ReportClass.call(this);
  this.dealPrice = 8;
  this.pickPrice = 12;
}
TmbReportClass.prototype = Object.create(ReportClass.prototype);

function LabReportClass() {
  ReportClass.call(this);
}
LabReportClass.prototype = Object.create(ReportClass.prototype);
