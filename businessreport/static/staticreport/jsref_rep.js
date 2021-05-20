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

    LabReportClass.prototype = Object.create(ReportClass.prototype);
    TmbReportClass.prototype = Object.create(ReportClass.prototype);
    KalimpReportClass.prototype = Object.create(ReportClass.prototype);
    //updates expenses table
    ReportClass.prototype.updateCost = function () {
        var totalCost = 0;
        var expenseAs = "";
        $("table tbody")
            .find("tr")
            .each(function (i, el) {
                if ($("table tbody tr").length - 2 == i) return false;
                var $tds = $(this).find("td"),
                    expense = $tds.eq(0).text(),
                    amt = $tds.eq(1).text();
                expenseAs += expense + " = " + amt + ";";
                totalCost += parseInt(amt);
            });
        expensesAsText = expenseAs;
        //write to hidden field expensesText and totalExpText for sending through the backend
        $("#expensesText").val(expensesAsText);
        $("#totalExpText").val(totalCost);
        $("#totalExpenses").html(totalCost);
        this.updateCTOCalc();
    };
    ReportClass.prototype.populateYesterValues = function () {
        $("#rndBeg").val(globalData["rndEnd"]);
        $("#cpSealBeg").val(globalData["capSealEnd"]);
        $("#sqSealBeg").val(globalData["sqSealEnd"]);
    };
    ReportClass.prototype.dealSalesChange = function () {
        deal = parseInt($("#dealText").val());
        $("#dealSales").html("P" + deal * this.dealPrice);
    };
    ReportClass.prototype.lessSalesChange = function () {
        deal = parseInt($("#dealText").val());
        less = parseInt($("#less").val());
        $("#dealSales").html("P" + (deal - less) * this.dealPrice);
    };
    ReportClass.prototype.pickSalesChange = function () {
        pick = parseInt($("#pickText").val());
        $("#pickSales").html("P" + pick * this.pickPrice);
    };
    ReportClass.prototype.smallSalesChange = function () {
        small = parseInt($("#smallText").val());
        $("#smallSales").html("P" + small * this.smallPrice);
    };
    ReportClass.prototype.rndSalesChange = function () {
        rnd = parseInt($("#rndText").val());
        $("#rndSales").html("P" + rnd * this.rndPrice);
    };
    ReportClass.prototype.squareSalesChange = function () {
        square = parseInt($("#squareText").val());
        $("#squareSales").html("P" + square * this.squarePrice);
    };
    LabReportClass.prototype.goodlySalesChange = function () {
        goodly = parseInt($("#squareText").val());
        $("#squareSales").html("P" + goodly * this.goodlyPrice);
    };
    KalimpReportClass.prototype.smallSquareSalesChange = function () {
        smallsquare = parseInt($("#smallSquare").val());
        $("#smallSquareSales").html("P" + smallsquare * this.smallSqPrice);
    };
    KalimpReportClass.prototype.bakeryGalSalesChange = function () {
        bakeryGal = parseInt($("#bakeryGal").val());
        $("#bakeryGalSales").html("P" + bakeryGal * this.bakeryPrice);
    };

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
        this.lessSalesChange();
        this.pickSalesChange();
        this.rndSalesChange();
        this.smallSalesChange();
        this.goodlySalesChange();
        this.squareSalesChange();
    };
    TmbReportClass.prototype.updateCTOCalc = function () {
        var ctoCalc =
            parseInt($("#dealText").val()) * this.dealPrice +
            parseInt($("#pickText").val()) * this.pickPrice +
            parseInt($("#rndText").val()) * this.rndPrice -
            parseInt($("#totalExpenses").html()) -
            parseInt($("#cashTkn").val());
        $("#ctoCalc").val(ctoCalc);
        this.dealSalesChange();
        this.pickSalesChange();
        this.rndSalesChange();
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
        this.lessSalesChange();
        this.pickSalesChange();
        this.rndSalesChange();
        this.smallSalesChange();
        this.squareSalesChange();
        this.smallSquareSalesChange();
        this.bakeryGalSalesChange();
    };
    var globalData = {};
    var globalClass = {};
    var locatio = $("h3.row").html(); //because location conflicts window.location
    if (locatio == "Talamban") {
        globalClass = new TmbReportClass();
    } else if (locatio == "Labangon") {
        globalClass = new LabReportClass();
    } else if (locatio == "Kalimpyo") {
        globalClass = new KalimpReportClass();
    }
    function isEmptyJSON(obj) {
        for (var prop in obj) {
            if (obj.hasOwnProperty(prop)) return false;
        }
        return true;
    }

    $("#ctoRep").change(function () {
        ctoCalc = parseInt($("#ctoCalc").val());
        ctoRep = parseInt($("#ctoRep").val());
        if (ctoCalc > ctoRep) {
            $("#isShortCTO").text(" Short ug " + (ctoCalc - ctoRep).toString());
        } else {
            $("#isShortCTO").text("");
        }
    });

    $("#cpSeal").change(function () {
        cpSeal = parseInt($("#cpSeal").val());
        cpSealYest = parseInt($("#cpSealBeg").val());
        cpSealCountCalc = cpSealYest - cpSeal;
        cpSealCountRep =
            parseInt($("#dealText").val()) +
            parseInt($("#pickText").val()) +
            parseInt($("#rndText").val());
        if (cpSealCountCalc > cpSealCountRep) {
            $("#isShortCapSl").text(
                " Short ug " + (cpSealCountCalc - cpSealCountRep).toString()
            );
        } else {
            $("#isShortCapSl").text("");
        }
    });

    $("#sqSeal").change(function () {
        sqSeal = parseInt($("#sqSeal").val());
        sqSealYest = parseInt($("#sqSealBeg").val());
        sqSealCountCalc = sqSealYest - sqSeal;
        sqSealCountRep = parseInt($("#squareText").val());
        if (sqSealCountCalc > sqSealCountRep) {
            $("#isShortSqSl").text(
                " Short ug " + (sqSealCountCalc - sqSealCountRep).toString()
            );
        } else {
            $("#isShortSqSl").text("");
        }
    });

    $("#rndEnd").change(function () {
        rndEnd = parseInt($("#rndEnd").val());
        rndYest = $("#rndBeg").val();
        rndCountCalc = rndYest - rndEnd;
        rndCountRep = parseInt($("#rndText").val());
        if (rndCountCalc > rndCountRep) {
            $("#isShortRnd").text(
                " Short ug " + (rndCountCalc - rndCountRep).toString()
            );
        } else {
            $("#isShortRnd").text("");
        }
    });

    $("#bdgMeter").change(function () {
        if (isEmptyJSON(globalData)) return;
        badgerToday = parseInt($("#bdgMeter").val());
        badgerYest = globalData["badgermeter"];
        badgerCalc = (badgerToday - badgerYest) * 2;
        badgerRep =
            parseInt($("#dealText").val()) +
            parseInt($("#pickText").val()) +
            parseInt($("#squareText").val()) +
            parseInt($("#bakeryGal").val()) +
            parseInt($("#smallText").val()) / 3 +
            parseInt($("#rndText").val());
        if (badgerCalc > badgerRep) {
            $("#isShortBadger").text(" Short ug " + (badgerCalc - badgerRep));
        } else {
            $("#isShortBadger").text("");
        }
    });

    $("#dateReport").change(function () {
        var dateReport = $("#dateReport").val();
        var crsf_value = document.querySelector("[name=csrfmiddlewaretoken]").value;
        $.ajax({
            url: "/ajax/get_data_yesterday/",
            data: {
                csrfmiddlewaretoken: crsf_value,
                dateReport: dateReport,
                location: locatio,
            },
            method: "POST",
            dataType: "json",
            success: function (data) {
                console.log(data);
                globalData = data;
                //if globaldata is not empty then populate textboxes
                if (!$.isEmptyObject(globalData)) globalClass.populateYesterValues();
            },
        });
    });

    $("[id^='duty']").change(function () {
        arra = [];
        $("[id^='duty']").each(function (i, e) {
            if (e.value != "") arra.push(e.value);
        });
        $("#duties").val(arra.join(","));
    });

    $("input[type]").on("click focusin", function () {
        this.value = "";
    });

    $("input[type=number]").on("blur", function () {
        if ($(this).val().trim().length == 0) {
            $(this).val("0");
        }
        globalClass.updateCTOCalc();
    });

    // Table jquery

    var actions = $("table td:last-child").html();
    // Append table with add row form on add new button click
    $(".add-new").click(function () {
        $(this).attr("disabled", "disabled");
        var index = $("table tbody tr:nth-last-child(2)").index();
        var row =
            "<tr>" +
            '<td><input type="text" class="form-control" name="name" id="name"></td>' +
            '<td><input type="text" class="form-control" name="department" id="department"></td>' +
            '<td><a class="add" title="Add"><i class="material-icons">&#xE03B;</i></a><a class="edit" title="Edit"><i class="material-icons">&#xE254;</i></a><a class="delete" title="Delete"><i class="material-icons">&#xE872;</i></a></td>' +
            "</tr>";
        $("table tr:nth-last-child(2)").before(row); //Insert row to 2nd to last child
        $("table tbody tr").eq(index).find(".add, .edit").toggle();
    });
    // Add row on add button click
    $(document).on("click", ".add", function () {
        var empty = false;
        var input = $(this).parents("tr").find('input[type="text"]');
        input.each(function () {
            if (!$(this).val()) {
                $(this).addClass("error");
                empty = true;
            } else {
                $(this).removeClass("error");
            }
        });
        $(this).parents("tr").find(".error").first().focus();
        if (!empty) {
            input.each(function () {
                $(this).parent("td").html($(this).val());
            });
            $(this).parents("tr").find(".add, .edit").toggle();
            $(".add-new").removeAttr("disabled");
        }
        globalClass.updateCost();
    });
    // Edit row on edit button click
    $(document).on("click", ".edit", function () {
        $(this)
            .parents("tr")
            .find("td:not(:last-child)")
            .each(function () {
                $(this).html(
                    '<input type="text" class="form-control" value="' +
                    $(this).text() +
                    '">'
                );
            });
        $(this).parents("tr").find(".add, .edit").toggle();
        $(".add-new").attr("disabled", "disabled");
    });
    // Delete row on delete button click
    $(document).on("click", ".delete", function () {
        $(this).parents("tr").remove();
        $(".add-new").removeAttr("disabled");
        globalClass.updateCost();
    });
});
