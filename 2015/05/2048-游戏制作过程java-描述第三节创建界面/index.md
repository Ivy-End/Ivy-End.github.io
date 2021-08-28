# 2048 游戏制作过程（Java 描述）：第三节、创建界面


首先，我们要使得我们的程序能够判断用户的手势，一共为上、下、左、右四种。在 GameView 类中添加如下代码：

```java
    private void initGameView() {
        setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {

                return false;
            }
        });
    }
```

接下来，我们来分析一下如何进行手势判断。首先，用户的手势输入应该有两个数据，一个是按下的屏幕位置，一个是放开的屏幕位置。那么我们只需要计算横向和竖向坐标差的绝对值，绝对值较大的一个方向则是用户需求的方向。至于横向中的左右和竖向中的上下，我们可以通过按下和放开的位置的大小进行比较得出。

有了上面的分析，我们开始写代码：

```java
    private void initGameView() {
        setOnTouchListener(new View.OnTouchListener() {

            private float startX, startY;   // 起始位置
            private float endX, endY;   // 终了位置
            private float offsetX, offsetY; // 偏移量
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                
                switch(event.getAction()) {
                    case MotionEvent.ACTION_DOWN:
                        startX = event.getX();
                        startY = event.getY();
                        break;
                    case MotionEvent.ACTION_UP:
                        endX = event.getX();
                        endY = event.getY();

                        offsetX = endX - startX;
                        offsetY = endY - startY;

                        if(Math.abs(offsetX) > Math.abs(offsetY)) { // 水平
                            if(offsetX < -5) {
                                System.out.println("Left");
                            } else if(offsetX > 5) {
                                System.out.println("Right");
                            }
                        } else { // 垂直
                            if(offsetX < -5) {
                                System.out.println("Up");
                            } else if(offsetX > 5) {
                                System.out.println("Down");
                            }
                        }
                }
                return false;
            }
        });
    }
```

运行程序，进入调试界面，如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_03.png" caption="阶段性效果" >}}

在窗口中用鼠标左滑，查看 Android Studio 中右下角 Logcat 窗口中的输出信息如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_04.png" caption="方向判断" >}}

说明我们的触摸检测已经成功了，接下来我们将四条输出语句换成四个函数。如下图所示：

```java
                        if(Math.abs(offsetX) > Math.abs(offsetY)) { // 水平
                            if(offsetX < -5) {
                                MoveLeft();
                            } else if(offsetX > 5) {
                                MoveRight();
                            }
                        } else { // 垂直
                            if(offsetX < -5) {
                                MoveUp();
                            } else if(offsetX > 5) {
                                MoveDown();
                            }
                        }
```

除此之外，我们还需要定义这四个函数，代码如下：

```java
    private void MoveLeft() {
        
    }

    private void MoveRight() {
        
    }

    private void MoveUp() {
        
    }

    private void MoveDown) {
        
    }
```

至于其中的处理方法，我们将在后续的章节中介绍。至此，我们的 GameView 框架基本能完成了。

接下来，我们使用上一节中的方法，创建一个 Card 类（用来显示游戏中的小方块以及其上的数字），并且让它继承自 FrameLayout，同时添加构造函数。如下图所示：

```java
package com.ivy.end.game2048;

import android.content.Context;
import android.widget.FrameLayout;

public class Card extends FrameLayout {

    public Card(Context context) {
        super context;
    }
}
```

此外，我们还需要创建几个私有成员变量，保存每张卡片上面的数字以及其它的一些信息：

```java
package com.ivy.end.game2048;

import android.content.Context;
import android.widget.FrameLayout;

public class Card extends FrameLayout {

    public Card(Context context) {
        super context;

        setNumber(0);   // 初始化数字为 0
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    private int number = 0;
}
```

接下来，我们还需要定义一个变量，用来显示文字，这里我们选用 TextView，代码如下：

```java
package com.ivy.end.game2048;

import android.content.Context;
import android.widget.FrameLayout;
import android.widget.TextView;

public class Card extends FrameLayout {

    public Card(Context context) {
        super context;

        // 初始化 tvNumber
        tvNumber = new TextView(getContext());
        tvNumber.setTextSize(32);

        // 添加 tvNumber
        LayoutParams lp = new LayoutParams(-1, -1);
        addView(tvNumber, lp);

        setNumber(0);   // 初始化数字为 0
    }

    public int getNumber() {
        return number;  // 返回数字
    }

    public void setNumber(int number) {
        this.number = number;   // 设置数字

        tvNumber.setText(number + "");  // 设置 tvNumber 文本
    }

    private int number = 0; // 保存数字
    private TextView tvNumber;  // 显示数字
}
```

接下去我们需要添加一些函数用来判断两个 Card 的值是否相等，以方便后期的折叠操作：

```java
    public boolean equals(Card o) {
        return getNumber() == o.getNumber();
    }
```

至此，我们游戏的基本元素已经基本完成，接下来我们需要进行组装。首先，我们需要获得卡片的宽高，这是由于不同手机分辨率不同，为了适配各类型的手机。在 GameView 中添加如下代码：

```java
    @Override
    protected void onSizeChanged(int w, int h, int oldw, int oldh) {
        super.onSizeChange(w, h, oldw, oldh);

        int cardSize = (Math.min(w, h) -10) / 4;    // 计算卡牌尺寸
        addCards(cardSize);
    }
```

除此之外，我们还需要添加一个 addCards 函数，将卡片添加进来：

```java
    private void addCards(int cardSize) {
        Card card;
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                card = new Card(getContext());
                card.setNumber(2);
                addView(card, cardSzie, cardSize);
            }
        }
    }
```

接着，我们需要将这个 GameView 调整为每行四列，在 initGameView 中添加如下代码：

```java
    private void initGameView() {
        
        setCOlumnCount(4);  // 设置列数
```

此时，我们可以运行来看一下效果：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_14.png" caption="阶段性效果" >}}

至此，我们已经完成了加入卡片的功能，接下来，我们需要使得卡牌居中放置，切换到 Card 类，修改构造函数代码如下：

```java
public class Card extends FrameLayout {

    public Card(Context context) {
        super context;

        // 初始化 tvNumber
        tvNumber = new TextView(getContext());
        tvNumber.setTextSize(32);
        tvNumber.setGravity(Gravity.CENTER);    // 居中

        // 添加 tvNumber
        LayoutParams lp = new LayoutParams(-1, -1);
        addView(tvNumber, lp);

        setNumber(0);   // 初始化数字为 0
    }
```

再测试一下，结果如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_16.png" caption="阶段性效果" >}}

接下来，我们需要添加背景，首先在 GameView 的 initGameView 中添加如下代码：

```java
    private void initGameView() {
        
        setCOlumnCount(4);  // 设置列数

        setBackgroundColor(0xFFBBADA0); // 设置背景
```

然后，我们为卡片设置背景，切换到 Card 的构造函数，添加如下代码：

```java
public class Card extends FrameLayout {

    public Card(Context context) {
        super context;

        // 初始化 tvNumber
        tvNumber = new TextView(getContext());
        tvNumber.setTextSize(32);
        tvNumber.setBackgroundColor(0x33FFFFFF); // 设置背景
        tvNumber.setGravity(Gravity.CENTER);    // 居中

        // 添加 tvNumber
        LayoutParams lp = new LayoutParams(-1, -1);
        addView(tvNumber, lp);

        setNumber(0);   // 初始化数字为 0
    }
```

运行结果如下：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_19.png" caption="阶段性效果" >}}

显示效果如上图，我们发现卡牌直接没有空格，看起来非常的紧凑，我们可以在 Card 类中这样修改代码：

```java
        // 添加 tvNumber
        LayoutParams lp = new LayoutParams(-1, -1);
        lp.setMargins(10, 10, 0, 0);    // 设置偏移量
        addView(tvNumber, lp);
```

再次运行程序，如下图所示：

{{< image src="/images/2015/2048 游戏制作过程（Java 描述）：第三节、创建界面/game2048_3_21.png" caption="阶段性效果" >}}

在下一节中，我们将介绍游戏的内部逻辑。
