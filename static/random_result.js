"use strict"; 

//prevent from going to new page with fave restaurant exists msg, target the form, not the id 

$('#add_fav').on('submit', (evt) => {
  evt.preventDefault();
  console.log(evt); 

  const formInputs = {
    'name': $('#name').val(),
    'address': $('#address').val(),
    'phone': $('#phone').val(),
    'url': $('#url').val(),  
    'image': $('#image').val(),
    'restaurant_id': $('#restaurant_id').val(),
}

// console.log(formInputs)
$.post('/create_favorite', formInputs, (response) => {
    // console.log(response);
    // console.log(response.name)

    if(response.length = 0)
    $('#list_content').append(`
      <li>${response.name} ${response.address} ${response.phone} ${response.url} 
      </li>
    `);
  });
    // else {$

    // }
  return "This has already been added to your favorites list!!!!"; 
}); 


//get new random result with pressing button 
$('#get_new_result').on('click', (evt) => {
    // evt.preventDefault();
    console.log('get new result clicked')
  $.get('/restaurant_result', (response) => {
    $('#restaurant_result').html(response);
  });
});


//if no fields are entered in log in fields, show error message 
$("#login_form").submit(function(evt){
    evt.preventDefault(); 

    var email  = $("#email").val(); 
    var password = $("#password").val(); 

    if(name == "" || password == "") {
        $("#error_message").show().html("All fields are required"); 
    } else {
        $("#error_message").html("").hide(); 
    }
})

//if logged in hide the create account fields 