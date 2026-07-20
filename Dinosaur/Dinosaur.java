import javax.swing.JFrame;

public class App {
    public static void main(String[] args) throws Exception {
        int altezza = 250;
        int lunghezza = 750;

        JFrame frame = new JFrame("Dinosaur");
        frame.setSize(lunghezza, altezza);
        frame.setLocationRelativeTo(null);
        frame.setResizable(false);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        

        ChromeDinosaur dino = new ChromeDinosaur();
        frame.add(dino);
        frame.pack();
        dino.requestFocus();
        frame.setVisible(true);
    }
}
