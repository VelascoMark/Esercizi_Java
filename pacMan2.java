import javax.swing.JFrame;// estensioni di pacchetti di java, non sono pacchetti creati da java direttamente

//la differenza tra JFrame e JPanel è che il frame è un contenitore che contiene i pannelli che possono essere modificati e "colorati"
public class App {
    public static void main(String[] args) throws Exception {
        int altezza = 21;
        int larghezza = 19;
        int pixels = 32;
        int widthPixel = larghezza * pixels;
        int heightPixel = altezza * pixels;

        JFrame frame = new JFrame("Pac Man");//crea una finestra con nome Pac Man
        frame.setSize(widthPixel, heightPixel);//imposta dimensione del frame in base pixel
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);//come parametro esplicito chiede un oggetto "Component" e in base a ciò centra il frame
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//si chiude cliccando X in alto a destra

        PacMan backGroundPanel = new PacMan();
        frame.add(backGroundPanel);
        frame.pack();//questo metodo serve per ridimensionar la finestra(frame) in base a ciò che ce dentro
        backGroundPanel.requestFocus();//riceve gli input da subito
        frame.setVisible(true);

    }
}
