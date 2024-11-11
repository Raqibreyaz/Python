function Sandbox(func) {
  return function (...params) {
    const start = Date.now();
    const result = func(...params);
    const end = Date.now();
    console.log(`${func.name} ran in ${end - start} time`);
    return result;
  };
}

const func1 = Sandbox((name, greeting="Hello") => {
  console.log(`${greeting} ${name}`);
});

func1("raquib","hello");
