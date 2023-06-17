$("#addAttend").click(function () {
  var index = $("#tableAttend tbody tr:nth-last-child(1)").index();
  var row =
    "<tr>" +
    '<td><input type="text" class="form-control" name="name" id="name"></td>' +
    '<td><a class="delete" title="Delete"><i class="material-icons">&#xE872;</i></a></td>' +
    "</tr>";
  $("#tableAttend tbody tr:nth-last-child(1)").before(row); //Insert row to 2nd to last child
  $("#tableAttend tbody tr").eq(index).find(".add, .edit").toggle();
});

$("#addHalin").click(function () {
  var index = $("#tableHalin tbody tr:nth-last-child(1)").index();
  var row =
    "<tr>" +
    '<td><input type="text" class="form-control" name="name" id="name"></td>' +
    '<td><input type="time" class="form-control" name="timePutos" id="timePutos"></td>' +
    '<td><input type="text" class="form-control" name="halin" id="halin"></td>' +
    '<td><a class="delete" title="Delete"><i class="material-icons">&#xE872;</i></a></td>' +
    "</tr>";
  $("#tableHalin tbody tr:nth-last-child(1)").before(row); //Insert row to 2nd to last child
  $("#tableHalin tbody tr").eq(index).find(".add, .edit").toggle();
});

$("#addStocks").click(function () {
  var index = $("#tableHalin tbody tr:nth-last-child(1)").index();
  var row =
    "<tr>" +
    '<td><input type="text" class="form-control" name="name" id="name"></td>' +
    '<td><input type="text" class="form-control" name="stocks" id="stocks"></td>' +
    '<td><a class="delete" title="Delete"><i class="material-icons">&#xE872;</i></a></td>' +
    "</tr>";
  $("#tableStocks tbody tr:nth-last-child(1)").before(row); //Insert row to 2nd to last child
  $("#tableStocks tbody tr").eq(index).find(".add, .edit").toggle();
});

$("#addExpenses").click(function () {
  var index = $("#tableExpenses tbody tr:nth-last-child(2)").index();
  var row =
    "<tr>" +
    '<td><input type="text" class="form-control" name="name" id="name"></td>' +
    '<td><input type="number" class="form-control" name="stocks" id="stocks"></td>' +
    '<td><a class="delete" title="Delete"><i class="material-icons">&#xE872;</i></a></td>' +
    "</tr>";
  $("#tableExpenses tbody tr:nth-last-child(2)").before(row); //Insert row to 2nd to last child
  $("#tableExpenses tbody tr").eq(index).find(".add, .edit").toggle();
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
    /* input.each(function () {
      $(this).parent("td").html($(this).val());
    }); */
    $(this).parents("tr").find(".add, .edit").toggle();
    $(".add-new").removeAttr("disabled");
  }
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
  //$(".add-new").attr("disabled", "disabled");
});

// Delete row on delete button click
$(document).on("click", ".delete", function () {
  $(this).parents("tr").remove();
  //$(".add-new").removeAttr("disabled");
});
