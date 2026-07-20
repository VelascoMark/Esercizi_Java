import javax.swing.*;
import java.util.Random;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class ChromeDinosaur extends JPanel implements KeyListener, ActionListener{
    
    private int altezza = 250;
    private int lunghezza = 750;

    //load images
    
    //Big Cactus
    private Image bigCactus1;
    private Image bigCactus2;
    private Image bigCactus3;
    //Normal Cactus
    private Image cactus1;
    private Image cactus2;
    private Image cactus3;
    //Birds
    private Image bird;
    private Image bird1;
    private Image bird2;
    private Image cloud;
    //dino
    private Image dinoDead;
    private Image dinoDuck;
    private Image dinoJump;
    private Image dinoRun;

    private Image reset;

    JButton resetButton;
    int dinosaurDuckHeight = 50;
    int duckCounter = 0; // Serve per il timer di 1 secondo
    boolean isDucking = false;


    public class Block{
        int x;
        int y;
        int height;
        int width;
        Image image;

        public Block(int x, int y, int height, int width, Image image){
            this.x = x;
            this.y = y;
            this.height = height;
            this.width = width;
            this.image = image;
        }
    }
    

    int dinosaurWidth = 88;
    int dinosaurHeight = 94;
    int dinosaurX = 50;
    int dinosaurY = altezza - dinosaurHeight;

    //cactus normali e grandi
    int cactus1width = 34;
    int cactus2width = 69;
    int cactus3width = 102;

    int cactusBigHeight = 85;
    int cactusHeight = 70;
    int cactusX = 700;
    int cactusY = altezza - cactusHeight;
    ArrayList<Block> cactusArray;

    Timer gameLoop;
    Timer placeCactusTimer;
    Timer placeCactusTimer2;

    //fisica
    int velocityX = -12;
    int velocityY = 0;
    int gravity = 1;
    int delay = 0;

    double score = 0;

    boolean gameOver = false;
    Block dinosaur;
    ChromeDinosaur(){
        setPreferredSize(new Dimension(lunghezza, altezza));
        setBackground(Color.LIGHT_GRAY);
        addKeyListener(this);//aggiunge un sensore che legge i segnali di input
        setFocusable(true);

        dinoDead = new ImageIcon(getClass().getResource("dino-dead.png")).getImage();
        dinoJump = new ImageIcon(getClass().getResource("dino-jump.png")).getImage();
        dinoRun = new ImageIcon(getClass().getResource("dino-run.gif")).getImage();
        dinoDuck = new ImageIcon(getClass().getResource("dino-duck.gif")).getImage();
        cactus1 = new ImageIcon(getClass().getResource("cactus1.png")).getImage();
        cactus2 = new ImageIcon(getClass().getResource("cactus2.png")).getImage();
        cactus3 = new ImageIcon(getClass().getResource("cactus3.png")).getImage();
        bigCactus1 = new ImageIcon(getClass().getResource("big-cactus1.png")).getImage();
        bigCactus2 = new ImageIcon(getClass().getResource("big-cactus2.png")).getImage();
        bigCactus3 = new ImageIcon(getClass().getResource("big-cactus3.png")).getImage();
        reset = new ImageIcon(getClass().getResource("reset.png")).getImage();
        
        dinosaur = new Block(dinosaurX, dinosaurY, dinosaurHeight, dinosaurWidth, dinoRun);
        cactusArray = new ArrayList<Block>();
        gameLoop = new Timer(1000/60, this);
        gameLoop.start();

        placeCactusTimer = new Timer(1500, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                placeCactus();
            }
        });
        placeCactusTimer.start();

        placeCactusTimer2 = new Timer(2600, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                placeBigCactus();
            }
        });
        placeCactusTimer2.start();
    }

    void placeCactus(){
        double cactusChance = Math.random() * 100;
        if(cactusChance > 90){
            Block cactus = new Block(cactusX, cactusY, cactus3width, cactusHeight, cactus3);
            cactusArray.add(cactus);
        }
        else if(cactusChance < 90 && cactusChance > 50){
            Block cactus = new Block(cactusX, cactusY, cactus2width, cactusHeight, cactus2);
            cactusArray.add(cactus);
        }
        else if(cactusChance < 50){
            Block cactus = new Block(cactusX, cactusY, cactus1width, cactusHeight, cactus1);
            cactusArray.add(cactus);
        }
    }

    public void placeBigCactus(){
        double chanceToSpawn = Math.random() * 100;
        if(chanceToSpawn > 75){
            if(score >= 50){
                double cactusChance2 = Math.random() * 100;
                if(cactusChance2 > 50){
                    Block cactus = new Block(cactusX, cactusY, cactus1width, cactusBigHeight, bigCactus2);
                    cactusArray.add(cactus);
                }
                else if(cactusChance2 < 50 && cactusChance2 > 40){
                    Block cactus = new Block(cactusX, cactusY, cactus2width, cactusBigHeight, bigCactus2);
                    cactusArray.add(cactus);
                }
                else if(cactusChance2 < 10){
                    Block cactus = new Block(cactusX, cactusY, cactus3width, cactusBigHeight, bigCactus3);
                    cactusArray.add(cactus);
                }
            }
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {}

    @Override
    public void keyPressed(KeyEvent e) {
        if(e.getKeyCode() == KeyEvent.VK_1){
        if(dinosaur.y + dinosaur.height >= altezza && !isDucking){
            isDucking = true;
            duckCounter = 20;
            dinosaur.image = dinoDuck;
            dinosaur.height = dinosaurDuckHeight;
            dinosaur.y = altezza - dinosaur.height; // Appoggia i piedi a terra
        }
    }
    }

    @Override
        public void keyReleased(KeyEvent e) {
        if(e.getKeyCode() == KeyEvent.VK_SPACE){
            if(dinosaur.y == dinosaurY){
                velocityY = -17;
                dinosaur.image = dinoJump;
            }
        }

        if(e.getKeyCode() == KeyEvent.VK_0){
            if(gameOver){
                cactusArray.removeAll(cactusArray);
                dinosaur.x = dinosaurX;
                dinosaur.y = dinosaurY;
                dinosaur.height = dinosaurHeight;
                dinosaur.width = dinosaurWidth;
                gameOver = false;
                setPreferredSize(new Dimension(lunghezza, altezza));
                setBackground(Color.LIGHT_GRAY);
                gameLoop.start();
            }
        }

    }

    public void move(){
    
    if (isDucking) {
        duckCounter--;
        if (duckCounter <= 0) {
            isDucking = false;
            dinosaur.height = dinosaurHeight;
            dinosaur.y = altezza - dinosaur.height;
            dinosaur.image = dinoRun; // Torna a correre
        }
    }

    // Gravità
    velocityY += gravity;
    dinosaur.y += velocityY;

    // Controllo collisione col suolo
    if(dinosaur.y + dinosaur.height > altezza){
        dinosaur.y = altezza - dinosaur.height;
        velocityY = 0;
        
        
        if (!isDucking && dinosaur.image != dinoRun) {
            dinosaur.image = dinoRun;
        }
    }

    
    for(int i = 0; i < cactusArray.size(); i++){
        Block cactus = cactusArray.get(i);
        cactus.x += (score >= 150) ? velocityX - 2 : velocityX;
        
        if(collision(dinosaur, cactus)){
            gameOver = true;
            dinosaur.image = dinoDead;
        }
    }
}

    public boolean collision(Block a, Block b){
        return a.x < b.x + b.width &&   
               a.x + a.width > b.x &&   
               a.y < b.y + b.height &&
               a.y + a.height > b.y;
    }

    public void paintComponent(Graphics g){
        super.paintComponent(g);
        draw(g);
    }

    public void draw(Graphics g){
        g.drawImage(dinosaur.image, dinosaur.x, dinosaur.y, dinosaur.width, dinosaur.height, null);

        for(int i = 0; i < cactusArray.size(); i++){
            Block cactus = cactusArray.get(i);
            g.drawImage(cactus.image, cactus.x, cactus.y, cactus.width, cactus.height, null);
            
        }

        g.setColor(Color.black);
        g.setFont(new Font("Courier", Font.PLAIN, 32));
        if (gameOver) {
            g.drawString("Game Over: " + String.valueOf(( int)score), 10, 35);
            setPreferredSize(new Dimension(lunghezza, altezza));
            setBackground(Color.RED);

        }
        else {
            g.drawString(String.valueOf((int)score), 10, 35);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        delay++;
        move();
        repaint();
        score = score + 0.2; 
        if(gameOver){
            gameLoop.stop();
            score = 0;
        }
    }
}
