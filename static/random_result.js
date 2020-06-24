"use strict"; 




//prevent from going to new page with fave restaurant exists msg

$('#favorite_btn').on('submit', (evt) => {
  evt.preventDefault();
  console.log(evt); 

  const formInputs = {
    'name': $('#name').val(),
    'address': $('#address').val(),
    'phone': $('#phone').val(),
    'location': $('#location').val()
  }

$.post('/create_favorite', formInputs, (response) => {
    console.log(response);
    $('#list_content').append(`
      <li>${response.name} ${response.address} ${response.phone} ${response.url} 
      </li>
    `);
  });
  return "This has already been added to your favorites list!!!!"; 
}); 


//get new random result with pressing button 
$('#get_new_result').on('click', (evt) => {
    evt.preventDefault();
    console.log('get new result clicked')
  $.get('/restaurant_result', (response) => {
    $('#restaurant_result').html(response);
  });
});


