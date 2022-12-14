use std::fs;

fn main() {
    let data_file_path = "/Users/gnuchu/projects/adventofcode2022/day1/data/data.txt";
    let todays_data = fs::read_to_string(data_file_path).expect("File contents read successfully");

    println!("Todayas data\n{todays_data}");
}
