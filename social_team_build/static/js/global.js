$( document ).ready(function() {

    $('textarea').autogrow({onInitialize: true});

    let positionForm = document.querySelectorAll('#position_form');
    let totalForms = document.querySelector('#id_form-TOTAL_FORMS');
    let formNum = positionForm.length - 1

    //Cloner for infinite input lists
    $(".circle--clone--list").on("click", ".circle--clone--add", function () {
        var parent = $(this).parent("li");
        var copy = parent.clone();
        let formRegex = RegExp(`form-(\\d){1}-`, 'g');

        parent.after(copy);
        copy.innerHTML = copy.innerHTML.replace(formRegex, 'form-${formNum}-1');
        document.write(copy.innerHTML)
        copy.find("input, textarea, select").val("");
        copy.find("*:first-child").focus();
        totalForms.setAttribute('value', '${formNum+1}')
    });

    $(".circle--clone--list").on("click", "li:not(:only-child) .circle--clone--remove", function () {
        var parent = $(this).parent("li");
        parent.remove();
    });

    // Adds class to selected item
    $(".circle--pill--list a").click(function () {
        $(".circle--pill--list a").removeClass("selected");
        $(this).addClass("selected");
  });

  // Adds class to parent div of select menu
  $(".circle--select select").focus(function(){
   $(this).parent().addClass("focus");
   }).blur(function(){
     $(this).parent().removeClass("focus");
   });

  // Clickable table row
  $(".clickable-row").click(function() {
      var link = $(this).data("href");
      var target = $(this).data("target");

      if ($(this).attr("data-target")) {
        window.open(link, target);
      }
      else {
        window.open(link, "_self");
      }
  });

  // Custom File Inputs
  var input = $(".circle--input--file");
  var text = input.data("text");
  var state = input.data("state");
  input.wrap(function() {
    return "<a class='button " + state + "'>" + text + "</div>";
  });




});