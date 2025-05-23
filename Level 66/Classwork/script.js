function compareNums(num1, num2) {
  console.log(`შედარება ${num1} და ${num2}:`);
  console.log(`${num1} > ${num2} =>`, num1 > num2);
  console.log(`${num1} >= ${num2} =>`, num1 >= num2);
  console.log(`${num1} < ${num2} =>`, num1 < num2);
  console.log(`${num1} <= ${num2} =>`, num1 <= num2);
  console.log(`${num1} == ${num2} =>`, num1 == num2);   
  console.log(`${num1} === ${num2} =>`, num1 === num2); 
  console.log(`${num1} != ${num2} =>`, num1 != num2);
  console.log(`${num1} !== ${num2} =>`, num1 !== num2);
}

compareNums(5, 10);
compareNums(20, '20');
compareNums(7, 7);


    const form = document.getElementById('myForm');

    form.addEventListener('submit', function(event) {
      event.preventDefault(); 
      
      const inputValue = form.elements['myInput'].value;
      alert('შეყვანილი მნიშვნელობაა: ' + inputValue);
    });