use sdl2::rect::Point;
use sdl2::render::WindowCanvas;
use nalgebra::Vector2;
use crate::ball::ball::Ball;
pub struct Wall {
    elasticity: f64,
    st_position: Vector2<f64>,
    ed_position: Vector2<f64>,
    wall_normal:Vector2<f64>,
    color: (u8, u8, u8),
    thickness: u32,
}

impl Wall {
    pub fn new(x1: f64, y1: f64, x2: f64, y2: f64) -> Self {
        let color = (rand::random::<u8>(), rand::random::<u8>(), rand::random::<u8>());
        let ab = Vector2::new(x2, y2) - Vector2::new(x1, y1);
        let mut y = Vector2::new(-ab.y, ab.x);
        y.normalize_mut();
        Wall {
            elasticity: 1.0,
            st_position: Vector2::new(x1, y1),
            ed_position: Vector2::new(x2, y2),
         wall_normal : y,
            color,
            thickness: 5,
        }
    }

    pub fn interact(&self, b: &mut Ball) {


        let wall_to_ball = b.position - self.st_position;

        let perpendicular_distance = wall_to_ball.dot(&self.wall_normal);

        if perpendicular_distance.abs() <= b.radius as f64 {
            let relative_velocity = (b.velocity).dot(&self.wall_normal);
            let penetration_depth = b.radius as f64 - perpendicular_distance.abs();

            b.position += penetration_depth * self.wall_normal;
            if relative_velocity > 0.0 {
                return;
            }

            let impulse_magnitude = -(1.0 + self.elasticity) * relative_velocity;

            let impulse = impulse_magnitude * self.wall_normal;

            b.velocity  += impulse;
        }
    }
    pub fn draw(&self, canvas: &mut WindowCanvas) {
        // Set the drawing color to the wall's color
        canvas.set_draw_color(self.color);

        // Draw a line representing the wall on the canvas
        canvas.draw_line(
            Point::new(self.st_position.x as i32, self.st_position.y as i32),
            Point::new(self.ed_position.x as i32, self.ed_position.y as i32),
        ).unwrap();
    }

    
}
