use nalgebra as na;
use rand::prelude::*;

pub fn vector_with_magnitude(mag: f64) -> na::Vector2<f64> {
    let mut rng = rand::thread_rng();
    let  vec_data = [rng.gen_range(-1.0..1.0), rng.gen_range(-1.0..1.0)];
    
    let norm_factor: f64 = vec_data.iter().map(|&x: &f64| x.powf(2.0)).sum::<f64>().sqrt() / mag;
    let normalized_vec: Vec<f64> = vec_data.iter().map(|&x| x / norm_factor).collect();
    na::Vector2::<f64>::from_row_slice(&normalized_vec)
}