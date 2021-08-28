# 2048 游戏制作过程（Java 描述）：第五节、界面美化


这一节，我们将介绍游戏界面的美化以及游戏数据的存储。

首先创建一个 color.xml 资源文件，用来保存每个数字对应的背景色和前景色。右击 res 文件夹，选择 New，单击 Android resource file，输入 color，单击 Next 即可。

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第五节、界面美化/game2048_5_01.png" caption="新建资源" >}}

修改代码如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="bg2">#eee4da</color>
    <color name="text2">#776e65</color>
    <color name="bg4">#ede0c8</color>
    <color name="text4">#776e65</color>
    <color name="bg8">#f2b179</color>
    <color name="text8">#f9f6f2</color>
    <color name="bg16">#f59563</color>
    <color name="text16">#f9f6f2</color>
    <color name="bg32">#f67c5f</color>
    <color name="text32">#f9f6f2</color>
    <color name="bg64">#f65e3b</color>
    <color name="text64">#f9f6f2</color>
    <color name="bg128">#edcf72</color>
    <color name="text128">#f9f6f2</color>
    <color name="bg256">#edcc61</color>
    <color name="text256">#f9f6f2</color>
    <color name="bg512">#edc850</color>
    <color name="text512">#f9f6f2</color>
    <color name="bg1024">#edc53f</color>
    <color name="text1024">#f9f6f2</color>
    <color name="bg2048">#edc22e</color>
    <color name="text2048">#f9f6f2</color>
    <color name="bgsuper">#3c3a32</color>
    <color name="textsuper">#f9f6f2</color>
</resources>
```

其中 bg 表示背景色，text 表示前景色，切换到 Card 界面，在 setNumber 中添加如下代码：

```java
            switch(number) {
                case 0:
                    tvNumber.setBackgroundColor(0x33FFFFFF);
                    break;
                case 2:
                    tvNumber.setTextColor(getResources().getColor(R.color.text2));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg2));
                    break;
                case 4:
                    tvNumber.setTextColor(getResources().getColor(R.color.text4));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg4));
                    break;
                case 8:
                    tvNumber.setTextColor(getResources().getColor(R.color.text8));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg8));
                    break;
                case 16:
                    tvNumber.setTextColor(getResources().getColor(R.color.text16));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg16));
                    break;
                case 32:
                    tvNumber.setTextColor(getResources().getColor(R.color.text32));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg32));
                    break;
                case 64:
                    tvNumber.setTextColor(getResources().getColor(R.color.text64));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg64));
                    break;
                case 128:
                    tvNumber.setTextColor(getResources().getColor(R.color.text128));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg128));
                    break;
                case 256:
                    tvNumber.setTextColor(getResources().getColor(R.color.text256));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg256));
                    break;
                case 512:
                    tvNumber.setTextColor(getResources().getColor(R.color.text512));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg512));
                    break;
                case 1024:
                    tvNumber.setTextColor(getResources().getColor(R.color.text1024));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg1024));
                    break;
                case 2048:
                    tvNumber.setTextColor(getResources().getColor(R.color.text2048));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bg2048));
                    break;
                default:
                    tvNumber.setTextColor(getResources().getColor(R.color.textsuper));
                    tvNumber.setBackgroundColor(getResources().getColor(R.color.bgsuper));
                    break;
            }
```

运行结果如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第五节、界面美化/game2048_5_05.png" caption="阶段性效果" >}}

游戏局面基本已经完成。接下来，我们来处理一下主界面的布局，切换到activity_main.xml的代码模式，修改如下：

```xml
<?xml version="1.0" encoding="utf-8">
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <LinearLayout
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:paddingTop="8dp"
        android:paddingBottom="8dp"
        android:layout_gravity="right">
    
        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="fill_parent"
            android:orientation="vertical"
            android:layout_marginLeft="16dp"
            android:layout_marginRight="8dp">

            <TextView
                android:layout_width="fill_parent"
                android:layout_height="wrap_content"
                android:text="@string/appname"
                android:textSize="84sp"
                android:textColor="#BBADA0"
                android:paddingTop="8dp"
                android:paddingBottom="8dp"
                android:paddingLeft="16dp"
                android:paddingRight="16dp"
                android:gravity="center" />

        </LinearLayout>

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="fill_parent"
            android:orientation="vertical"
            android:layout_marginLeft="16dp"
            android:layout_marginRight="8dp">

            <TextView
                android:layout_width="fill_parent"
                android:layout_height="wrap_content"
                android:text="@string/score"
                android:textSize="42sp"
                android:textColor="#BBADA0"
                android:paddingTop="8dp"
                android:paddingBottom="8dp"
                android:paddingLeft="16dp"
                android:paddingRight="16dp"
                android:gravity="center" />

            <TextView
                android:id="@+id/tvScore"
                android:layout_width="fill_parent"
                android:layout_height="wrap_content"
                android:textSize="42sp"
                android:textColor="#BBADA0"
                android:paddingTop="8dp"
                android:paddingBottom="8dp"
                android:paddingLeft="16dp"
                android:paddingRight="16dp"
                android:gravity="center" />

        </LinearLayout>

    </LinearLayout>

    <GridLayout
        android:id="@+id/gameView"
        android:layout_width="fill_parent"
        android:layout_height="0dp"
        android:layout_weight="1">
    <GridLayout>

</LinearLayout>
```

运行结果如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第五节、界面美化/game2048_5_10.png" caption="阶段性效果" >}}

下面，我们需要为 Best 标签添加一些操作，切换到 MainActivity 类，定义一个变量：

```java
    private void score = 0;
    private TextView tvScore;
    private TextView tvBest;
    private static MainActivity mainActivity = null;
```

为它添加初始化命令：

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvScore = (TextView)findViewById(R.id.tvScore);
        tvBest = (TextView)findViewById(R.id.tvBest);

        mainActivity = this;
    }
```

添加一个方法方便外部访问这个标签，同时定义一个 bestScore 变量用来保存最高分：

```java
    public void showScore() {
        tvScore.setText(score + "");
        tvBest.setText(bestScore + "");
    }

    public void addScore(int s) {
        score += s;
        showScore();
    }

    public int getScore() {
        return score;
    }

    public void setBestScore(int s) {
        bestScore = s;
        showScore();
    }

    private int score = 0;
    private int bestScore = 0;
    private TextView tvScore;
    private TextView tvBest;
    private static MainActivity mainActivity = null;
```

切换到 GameView 中添加如下方法：

```java
    private void updateBest() {
        int bestScore, score;
        SharedPreferences sp = getContext().getSharedPreferences("game2048", Context.MODE_PRIVATE);
        SharedPreferences.Editoer editor = sp.edit();
        score = MainActivity.getMainActivity().getScore();
        bestScore = sp.getInt("best", 0);
        if (bestScore < score) {
            editor.putInt("best", score);
            MainActivity.getMainActivity().setBestScore(score);
            editor.commit();
        }
    }
```

在每一次加分后都调用该函数：

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
                        updateBest();   // 更新最高分
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
                        updateBest();   // 更新最高分
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
                        updateBest();   // 更新最高分
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
                        updateBest();   // 更新最高分
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

最后，我们需要对最高分标签进行初始化，切换到 MainActivity 类，修改代码如下：

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tvScore = (TextView)findViewById(R.id.tvScore);
        tvBest = (TextView)findViewById(R.id.tvBest);

        SharedPreferences sp = getSharedPreferences("game2048", Contex.MODE_PRIVATE);

        bestScore = sp.getInt("best", 0);
        tvBest.setText(bestScore + "");

        mainActivity = this;
    }
```

运行结果如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第五节、界面美化/game2048_5_17.png" caption="运行效果" >}}

游戏至此已经完工。当然，我们可以为它添加更多的动画特效，留给读者自行操作。
