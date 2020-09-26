
var op1, op2;
var currOperator;

function operador(idd) {
	op1 = document.getElementById("visor").innerHTML;
	switch (idd) {
		case "bsoma":
			currOperator="+";
			break;
		case "bsubtracao":
			currOperator="-";
			break;
		case "bdivisao":
			currOperator="/";
			break;
		case "bmultiplicacao":
			currOperator="*";
			break;
	}
	document.getElementById("visor").innerHTML = currOperator;
}

function resultado() {
	if(op1!=undefined){
		op2 = document.getElementById("visor").innerHTML;
		op1 = parseFloat(op1)
		op2 = parseFloat(op2)
		switch(currOperator) {
			case "+":
				r = op1 + op2;
				break;
			case "-":
				r = op1 - op2;
				break;
			case "*":
				r = op1 * op2;
				break;
			case "/":
				r = op1 / op2;
				break;
		}
		if(op2==0 && currOperator=="/"){
			alert("Não divida por 0!! Poxa :/")
			document.getElementById("visor").innerHTML = "0"
		} else {
			if(r%1 != 0) {
				r = r.toPrecision(8)
			}
			document.getElementById("visor").innerHTML = r;
		}
		op1=undefined;
		op2=undefined;
		currOperator=undefined;
	}
}

function cleear() {
	document.getElementById("visor").innerHTML = 0;
	currOperator = undefined;
	op1 = undefined;
	op2 = undefined;
}

function botao_numero(idd) {
	numero_s = document.getElementById(idd).innerHTML
	visorAtual = document.getElementById("visor").innerHTML
	if(visorAtual == "0" || visorAtual == "+" || visorAtual == "-" ||
		visorAtual == "*" || visorAtual == "/"){
		document.getElementById("visor").innerHTML = numero_s;
	} else {
		if (visorAtual.length >= 10) {
			return ;
		} else {
			document.getElementById("visor").innerHTML += numero_s;
		}
	}
}

function btPonto() {
	document.getElementById("visor").innerHTML += ".";
}

function positivoNegativo() {
	visorAtual = document.getElementById("visor").innerHTML
	if(visorAtual == "0" || visorAtual == "+" || visorAtual == "-" ||
		visorAtual == "*" || visorAtual == "/"){
		return ;
	} else {
		if(visorAtual.search("-") == -1){
			document.getElementById("visor").innerHTML = "-" + visorAtual;
		} else {
			document.getElementById("visor").innerHTML = visorAtual.substring(1);
		}
	}
}
