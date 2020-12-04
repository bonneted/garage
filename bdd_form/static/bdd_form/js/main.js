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
}

function show_reparation(evt) {
  toggle = evt.currentTarget.checked
  if(toggle){
    document.getElementById("nom_reparation").style.display = ''
  }else{
    document.getElementById("nom_reparation").style.display = 'none'
  }
  // document.getElementById("nom_reparation").style.display = ''
  
}

function modifier_reparation(event) {
  var reparation = event.currentTarget
  console.log(reparation.value,reparation.innerHTML)
  var modif_form = document.getElementById("reparation_form").cloneNode(true);
  modif_form.getElementsByTagName('h1')[0].innerHTML = "Modifier la réparation";
  modif_form.style.position = 'absolute'
  modif_form.style.left = '50%'
  modif_form.style.top = '10%'
  modif_form.style.border = 'solid 2px hsl(204, 86%, 53%)'
  
  $('select[name ="technicien_id"]').value = reparation.technicien.id

  evt.currentTarget.parentNode.parentNode.parentNode.appendChild(modif_form);
}



$('#buttonRechClient').on('click', recherche);
$('#textRechClient').on('focusout', recherche); 
$('#textRechClient').on('keypress',function(e) {if(e.which == 13) {recherche(e)}});

$('#buttonRechVoiture').on('click', recherche);
$('#textRechVoiture').on('focusout', recherche); 
$('#textRechVoiture').on('keypress',function(e) {if(e.which == 13) {recherche(e)}});


$('#buttonRechReparation').on('click', recherche);
$('#textRechReparation').on('focusout', recherche); 
$('#textRechReparation').on('keypress',function(e) {if(e.which == 13) {recherche(e)}});

$('#ajout_piece').on('click', ajout_piece);

$('#reparation_standard').on('click', show_reparation);

var modif_rep = document.getElementsByClassName("button is-small is-info modifier_reparation")
console.log(modif_rep)

const loading_status = JSON.parse(document.getElementById('loading_status').textContent);
console.log(loading_status)

var delete_buttons = document.getElementsByClassName("delete");
for (var i = 0; i < delete_buttons.length; i++) {
  delete_buttons[i].addEventListener('click', hide_parent, false);
}

// tab gestion

function openPage(pageName,elmnt) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
    tablinks[i].style.color = "white";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = '#f5f5f5';
  elmnt.style.color = 'black';
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

{/* <div class="notification is-success is-fullwidth" style="positiontext-align: center;">
<button class="delete"></button>
Le client a bien été ajouté !
</div> */}