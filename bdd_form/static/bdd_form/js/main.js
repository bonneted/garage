function hide_parent(evt) {
  evt.currentTarget.parentNode.style.display = 'none';
}
function suppr_parent(evt) {
  var parent = evt.currentTarget.parentNode.parentNode;
  parent.parentNode.removeChild(parent);
}

var delete_buttons = document.getElementsByClassName("delete");
for (var i = 0; i < delete_buttons.length; i++) {
  delete_buttons[i].addEventListener('click', hide_parent, false);
}

function recherche(evt) {
  let parent_block =  evt.currentTarget.parentNode.parentNode;
  let ancestor_block = parent_block.parentNode.parentNode;
  
  console.log(parent_block)
  let txt_recherche = parent_block.getElementsByTagName("input")[0].value;
  var rows = ancestor_block.getElementsByTagName("table")[0].rows;

  for (var ii = 2; ii < rows.length; ii++) {
    var row_cells = rows[ii].cells;
    var row = rows[ii];
    var row_content = "";
    for (var kk = 0; kk < row_cells.length - 1; kk++) {
      row_content += row_cells[kk].innerHTML;
    }
    row_content = row_content.toLowerCase();

    if (row_content.includes(txt_recherche.toLowerCase())) {
      row.style.display = "";
    } else {
      row.style.display = "none";
    }
  }
}

function ajout_piece(evt) {
  var nouv_piece = document.getElementById("piece_field").cloneNode(true);
  nouv_piece.style.display = ''
  evt.currentTarget.parentNode.parentNode.parentNode.appendChild(nouv_piece);
  console.log(nouv_piece)
}

function myFunction() {

}

$('#buttonRechClient').on('click', recherche);
$('#textRechClient').on('focusout', recherche); 
$('#textRechClient').on('keypress',function(e) {if(e.which == 13) {recherche(e)}});

$('#buttonRechVoiture').on('click', recherche);
$('#textRechVoiture').on('focusout', recherche); 
$('#textRechVoiture').on('keypress',function(e) {if(e.which == 13) {recherche(e)}});

$('#ajout_piece').on('click', ajout_piece);


const loading_status = JSON.parse(document.getElementById('loading_status').textContent);
console.log(loading_status)




