$(document).ready(function(){ 
    var loadForm = function () { 
        var btn = $(this); 
        $.ajax({ 
          url: btn.attr("data-url"), 
          type: "get", 
          dataType: "json", 
          beforeSend: function () { 
            $("#modal-entity1 .modal-content").html(""); 
            $("#modal-entity1").modal("show"); 
          }, 
          success: function (data) { 
            $("#modal-entity1 .modal-content").html(data.html_form); 
          } 
        }); 
    }; 

    var saveForm = function () { 
        var form = $(this); 
        $.ajax({ 
          url: form.attr("action"), 
          data: form.serialize(), 
          type: form.attr("method"), 
          dataType: "json", 
          success: function (data) { 
            if (data.form_is_valid) { 
              $("#entity1-table tbody").html(data.html_entity1_list); 
              $("#modal-entity1").modal("hide"); 
            } 
            else { 
              $("#modal-entity1 .modal-content").html(data.html_form); 
            } 
          } 
        }); 
      return false; 
    }; 

    // Binding 
    $(".js-create-entity1").click(loadForm); 
    $("#modal-entity1").on("submit", ".js-entity1-create-form", saveForm); 

    // Update entity 
    $("#entity1-table").on("click", ".js-update-entity1", loadForm); 
    $("#modal-entity1").on("submit", ".js-entity1-update-form", saveForm); 

    // Delete entity 
    $("#entity1-table").on("click", ".js-delete-entity1", loadForm); 
    $("#modal-entity1").on("submit", ".js-entity1-delete-form", saveForm); 

}); 
