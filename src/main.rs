use std::time::{Duration, Instant}; 
extern crate sdl2;
use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use sdl2::pixels::Color;
mod simulation;
use simulation::Simulation;
mod ball;
mod wall;
mod utils;
fn main() {
    // Initialize SDL2
    let sdl_context = sdl2::init().unwrap();
    let video_subsystem = sdl_context.video().unwrap();
    let target_frame_duration = Duration::from_secs(1) / 60;

    // Create a window
    let window = video_subsystem
        .window("rust-sdl2 example", 800, 600)
        .opengl()
        .build()
        .map_err(|e| e.to_string())
        .unwrap();

    // Create a canvas
    let mut canvas = window.into_canvas().build().map_err(|e| e.to_string()).unwrap();
    let mut last_frame_time = Instant::now();
    let mut simulation = Simulation::new((800,600));
    
    
    
    

    // Main loop
    'main: loop {
        for event in sdl_context.event_pump().unwrap().poll_iter() {
            match event {
                Event::Quit { .. } | Event::KeyDown { keycode: Some(Keycode::Escape), .. } => {
                    break 'main;
                }
                _ => {}
            }
        }

        // Set the background color
        canvas.set_draw_color(Color::RGB(255, 200, 0));
        
        canvas.clear();
        simulation.update(1.0/60.0);
        simulation.draw(&mut canvas);

        // Present the canvas
        canvas.present();

        let elapsed_time = Instant::now() - last_frame_time;
        if elapsed_time < target_frame_duration {
            // std::thread::sleep(target_frame_duration - elapsed_time);
            
        }
        println!("{:?}",Instant::now() - last_frame_time);
        // Update last frame time
        last_frame_time = Instant::now();
    }
}
