static INPUT: &str = include_str!("../assets/day06.txt");


fn calc_fishes(days: usize, inp: &str) -> u64 {
    let initial_fishes: Vec<u64> = inp.split(',').map(|n| n.parse().unwrap()).collect();
    let mut table : Vec<u64> = (0..9).map(|n: u64| initial_fishes.iter().filter(|&k| *k == n).count() as u64).collect();
    for _ in 0..days {
        table[7] += table[0];
        table.rotate_left(1);
    }
    table.iter().sum()
}

pub fn part_a() -> String {
    calc_fishes(80 ,INPUT).to_string()
}
pub fn part_b() -> String {
    calc_fishes(256,INPUT).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static SAMPLE_INPUT: &str = include_str!("../assets/day06-sample.txt");
    #[test]
    fn example_a() {
        assert_eq!(calc_fishes(80,SAMPLE_INPUT), 5934);
    }

    #[test]
    fn example_b() {
        assert_eq!(calc_fishes(256,SAMPLE_INPUT), 26984457539);
    }
}