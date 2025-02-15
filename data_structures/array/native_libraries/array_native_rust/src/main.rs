fn main() {
    let mut arr = vec![1, 2, 3, 4];
    arr.push(5);  // Agregar elemento
    println!("{}", arr[2]);  // Acceder al índice 2


    let mut array: [i32; 3] = [0; 3];
    array[1] = 1;
    array[2] = 2;

    // This loop prints: 0 1 2
    for x in array {
        print!("{x} ");
    }
}