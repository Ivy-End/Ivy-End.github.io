# 2048 游戏制作过程（Java 描述）：第四节、游戏逻辑


上一节中，我们已经成功的将卡牌添加到了游戏中，但只是显示在了界面上，并没有保存下来。我们在 GameView 中定义一个二维数组用来保存游戏界面的卡牌。

```java
    private Card[][] cardMap = new Card[4][4];  // 记录游戏
```

接下来，我们需要将初始化时候添加的卡片添加到 cardMap 数组中，如下图所示：

```java
    private void addCards(int cardSize) {
        Card card;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                card = new Card(getContext());
                card.setNumber(2);
                addView(card, cardSzie, cardSize);
                cardMap[i][j] = card;   // 添加卡片
            }
        }
    }
```

这样一来，我们就将游戏界面记录下来了。

但是上一节中，我们一下子就生成了 16 张卡片，这和平时游戏的时候不一致。而且我们只能生成卡片 2。为了改进它，我们可以定义一个函数 addRandomNumber，表示每次生成的数字（这里我们设置生成 2 和 4 的概率为 9:1）：

```java
    private void addRandomNumber() {

        emptyPoints.clear();

        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(cardMap[i][j].getNumber() <= 0) {    // 用 0 表示空点
                    emptyPoints.add(new Point(i, j));
                }
            }
        }

        Point point = emptyPoints.remove((int)(Math.random() * emptyPoints.size()));    // 随机获取空点
        cardMap[point.x][point.y].setNumber(Math.random() > 0.1 ? 2 : 4);   // 按 9:1 的概率生成 2 和 4
    }
```

这里用到了一个 emptyPoints 变量，我们需要定义如下：

```java
    private Card[][] cardMap = new Card[4][4];  // 记录游戏
    private ListL<Point> emptyPoints = new ArrayList<>();   // 空点列表
```

除此之外，我们还看到在上面的程序中，我们使用 0 表示空点，但是我们并不希望 0 显示在我们的游戏中，因此修改 Card 类的 SetNumber 函数如下：

```java
    public void setNumber(int number) {
        this.number = number;   // 设置数字

        if(number > 0) {
            tvNumber.setText(number + "");  // 设置 tvNumber 文本
        } else {
            tvNumber.setText("");  // 空文本，不显示数字 0
        }
    }
```

同时，我们需要修改 GameView 中的 addCards 函数，使得一开始都生成空点：

```java
    private void addCards(int cardSize) {
        Card card;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                card = new Card(getContext());
                card.setNumber(0);  // 生成空点
                addView(card, cardSzie, cardSize);
                cardMap[i][j] = card;   // 添加卡片
            }
        }
    }
```

接下来，我们可以开始游戏了，首先定义一个 startGame 函数，同时在 onSizeChanged 事件中调用它，如下图所示：

```java
    @Override
    protected void onSizeChanged(int w, int h, int oldw, int oldh) {
        super.onSizeChange(w, h, oldw, oldh);

        int cardSize = (Math.min(w, h) -10) / 4;    // 计算卡牌尺寸
        addCards(cardSize);

        startGame();    // 开始游戏
    }
```

同时，定义 startGame 函数如下图所示：

```java
    private void startGame() {
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cardMap[i][j].setNumber(0); // 清空游戏界面
            }
        }

        // 初始化两张卡片
        addRandomNumber();
        addRandomNumber();
    }
```

运行查看结果，如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第四节、游戏逻辑/game2048_4_09.png" caption="阶段性效果" >}}

接下来，我们需要实现游戏的逻辑，也就是方块的合并。我们需要操作 MoveLeft 等四个函数。如下图所示：

```java
    private void MoveLeft() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 0; j < 4; j++) {    // 列循环
                for(int y = j + 1; y < 4; y++) {    // 从当前位置往右扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，左移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 左移，合并
                        cardMap[i][y].setNumber(0); // 清空
                    }
                }
            }
        }
    }
```

接下来的三个方向的移动只需要对上面的代码进行稍微修改即可，MoveRight 如下图所示：

```java
    private void MoveRight() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 3; j >= 0; j--) {    // 列循环
                for(int y = j - 1; y >= 0; y--) {    // 从当前位置往左扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，右移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 右移，合并
                        cardMap[i][y].setNumber(0); // 清空
                    }
                }
            }
        }
    }
```

MoveUp 函数如下图所示：

```java
    private void MoveUp() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 0; i < 4; i++) {    // 行循环
                for(int x = i + 1; x < 4; x++) {    // 从当前位置往下扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，上移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 上移，合并
                        cardMap[x][j].setNumber(0); // 清空
                    }
                }
            }
        }
    }
```

MoveDown 函数如下图所示：

```java
    private void MoveDown() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 3; i >= 0; i--) {    // 行循环
                for(int x = i - 1; x >= 0; x--) {    // 从当前位置往上扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，下移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 下移，合并
                        cardMap[x][j].setNumber(0); // 清空
                    }
                }
            }
        }
    }
```

至此，我们的移动功能已基本完成，测试如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第四节、游戏逻辑/game2048_4_14.png" caption="阶段性效果" >}}

最后，我们来完成积分的模块，每次操作得分都等于合并方块的数字之和。切换到 MainActivy 类，添加以下代码以获取 tvScore 这个标签：

```java
public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvScore = (TextView)findViewById(R.id.tvScore);
    }

    private TextView tvScore;
}
```

接下去，为了能够在外界操作 MainActivy 中的 tvScore，我们修改代码如下：

```java
public class MainActivity extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvScore = (TextView)findViewById(R.id.tvScore);

        mainActivity = this;
    }

    public static MainActivity getMainActivity() {
        return mainActivity;
    }

    private TextView tvScore;
    private static MainActivity mainActivity = null;
}
```

最后添加计分变量以及相关的操作函数：

```java
    public void clearScore() {
        score = 0;
        showScore();
    }

    public void showScore() {
        tvScore.setText(score + "");
    }

    public void addScore(int s) {
        score += s;
        showScore();
    }

    private int score = 0;
    private TextView tvScore;
    private static MainActivity mainActivity = null;
```

接下去，切换到 GameView 中，将下面的代码添加到四个移动操作的相应位置：

```java
    private void MoveLeft() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 0; j < 4; j++) {    // 列循环
                for(int y = j + 1; y < 4; y++) {    // 从当前位置往右扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，左移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 左移，合并
                        cardMap[i][y].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                    }
                }
            }
        }
    }
```

```java
    private void MoveRight() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 3; j >= 0; j--) {    // 列循环
                for(int y = j - 1; y >= 0; y--) {    // 从当前位置往左扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，右移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 右移，合并
                        cardMap[i][y].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                    }
                }
            }
        }
    }
```

```java
    private void MoveUp() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 0; i < 4; i++) {    // 行循环
                for(int x = i + 1; x < 4; x++) {    // 从当前位置往下扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，上移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 上移，合并
                        cardMap[x][j].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                    }
                }
            }
        }
    }
```

```java
    private void MoveDown() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 3; i >= 0; i--) {    // 行循环
                for(int x = i - 1; x >= 0; x--) {    // 从当前位置往上扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，下移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 下移，合并
                        cardMap[x][j].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                    }
                }
            }
        }
    }
```

接下来，我们需要在开始的时候清空分数：

```java
    private void startGame() {

        MainActivity.getMainActivity().clearScore();    // 清零

        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cardMap[i][j].setNumber(0); // 清空游戏界面
            }
        }

        // 初始化两张卡片
        addRandomNumber();
        addRandomNumber();
    }
```

运行测试：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第四节、游戏逻辑/game2048_4_20.png" caption="阶段性效果" >}}

接下去，我们需要在每次操作后都添加新的卡片：

```java
    private void MoveLeft() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 0; j < 4; j++) {    // 列循环
                for(int y = j + 1; y < 4; y++) {    // 从当前位置往右扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，左移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 左移，合并
                        cardMap[i][y].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                        move = true;    // 已操作
                    }
                }
            }
        }

        if(move) {  // 如果操作，添加新的卡片
            addRandomNumber();
        }
    }
```

```java
    private void MoveRight() {
         for(int i = 0; i < 4; i++) {   // 行循环
            for(int j = 3; j >= 0; j--) {    // 列循环
                for(int y = j - 1; y >= 0; y--) {    // 从当前位置往左扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[i][y].getNumber()); // 空位，右移
                        cardMap[i][y].setNumber(0); // 清空
                        y = j - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[i][y])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 右移，合并
                        cardMap[i][y].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                        move = true;    // 已操作
                    }
                }
            }
        }

        if(move) {  // 如果操作，添加新的卡片
            addRandomNumber();
        }
    }
```

```java
    private void MoveUp() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 0; i < 4; i++) {    // 行循环
                for(int x = i + 1; x < 4; x++) {    // 从当前位置往下扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，上移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i + 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 上移，合并
                        cardMap[x][j].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                        move = true;    // 已操作
                    }
                }
            }
        }

        if(move) {  // 如果操作，添加新的卡片
            addRandomNumber();
        }
    }
```

```java
    private void MoveDown() {
         for(int j = 0; j < 4; j++) {   // 列循环
            for(int i = 3; i >= 0; i--) {    // 行循环
                for(int x = i - 1; x >= 0; x--) {    // 从当前位置往上扫描
                    if(cardMap[i][j].getNumber() <= 0)  // 当前值为 0
                        cardMap[i][j].setNumber(cardMap[x][j].getNumber()); // 空位，下移
                        cardMap[x][j].setNumber(0); // 清空
                        x = i - 1;  // 避免 2 0 2 不合并的情况
                    } else if(cardMap[i][j].equals(cardMap[x][j])) {    // 相同
                        cardMap[i][j].setNumber(cardMap[i][j].getNumber() * 2); // 下移，合并
                        cardMap[x][j].setNumber(0); // 清空
                        MainActivity.getMainActivity().addScore(cardMap[i][j].getNumber()); // 加分
                        move = true;    // 已操作
                    }
                }
            }
        }

        if(move) {  // 如果操作，添加新的卡片
            addRandomNumber();
        }
    }
```

其它三种情况请读者自行根据上述代码进行修改。测试结果如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第四节、游戏逻辑/game2048_4_22.png" caption="阶段性效果" >}}

最后，我们还需要判断游戏是否结束。游戏结束的条件是没有空位并且无法继续合并。定义一个函数 checkGame，checkGame 函数实现如下：

```java
    private void checkGame() {

        boolean complete = true;    // 默认游戏结束

        ALL:
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                if(cardMap[i][j].getNumber() <= 0 ||
                    (i > 0 && cardMap[i][j].equals(cardMap[i - 1][j])) ||
                    (i < 3 && cardMap[i][j].equals(cardMap[i + 1][j])) ||
                    (j > 0 && cardMap[i][j].equals(cardMap[i][j - 1])) ||
                    (j < 3 && cardMap[i][j].equals(cardMap[i][j + 1]))) {
                    complete = false;   // 游戏未结束
                    break ALL;
                }
            }
        }

        if(complete) {
            new AlertDialog.Builder(getContext()).setTitle("2048").setMessage("游戏结束").setPositiveButton("重新开始",
                new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    startGame();    // 重新开始
                }
            }).show();
        }
```

至此，游戏的基本框架都已经全部完成，我们将在下一节中介绍分数的保存以及界面的美化。
