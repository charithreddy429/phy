use sdl2::render::WindowCanvas;
use crate::ball::ball_set::BallSet;
use crate::wall::Wall;


use crate::ball::ball::Ball;
use crate::utils;

pub struct Simulation {
    ballset: BallSet,
    walls: Vec<Wall>, // Add a vector of walls
    boundary: (i32, i32),
}

impl Simulation {
    pub fn new(boundary: (i32, i32)) -> Simulation {
        let ballset = BallSet::new((0..20).flat_map(|i| {
            (0..20).map(move |j| {
                Ball::new(
                    (20 + 20 * i) as f64,
                    (20 + 20 * j) as f64,
                    utils::vector_with_magnitude(100.0),
                )
            })
        }).collect());

        // Create some walls
        let walls = vec![
            Wall::new(0.0, 0.0, 800.0, 0.0),    // Top wall
            Wall::new(800.0, 0.0, 800.0, 600.0),    // Left wall
            Wall::new(800.0, 600.0, 0.0, 600.0),// Right wall
            Wall::new(0.0, 600.0, 0.0,0.0),// Bottom wall
            // Add more walls as needed
        ];

        Simulation {
            ballset,
            walls,
            boundary,
        }
    }

    pub fn update(&mut self,dt:f64) {
        self.ballset.update(dt);
        for wall in &self.walls {
            for ball in &mut self.ballset.balls {
                wall.interact(ball);
            }
        }
    }

    pub fn draw(&mut self, canvas: &mut WindowCanvas) {
        self.ballset.draw(canvas);
        // Draw walls
        for wall in &self.walls {
            wall.draw(canvas);
        }
    }
}
