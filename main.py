import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper
df = pd.read_excel('your exel name with suffix')
data = pd.to_datetime(df['به عنوان مثال:تاریخ فروش محصولات'])
data_1 = df.groupby(df['به عنوان مثال:تاریخ فروش محصولات'].dt.strftime('%Y-%A'))['مثال:تعداد فروش محصولات'].sum()
text_to_be_reshaped = 'مثال: توزیع فروش در هفته'
reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
bidi_text = get_display(reshaped_text)
text_to_be_reshaped1 = 'مثال: تاریخ سفارش'
reshaped_text1 = arabic_reshaper.reshape(text_to_be_reshaped1)
bidi_text1 = get_display(reshaped_text1)
text_to_be_reshaped2 = 'مثال: تعداد فروش'
reshaped_text2 = arabic_reshaper.reshape(text_to_be_reshaped2)
bidi_text2 = get_display(reshaped_text2)
data_1.plot(kind='bar', figsize=(25,15),rot=0,color='#054907')
plt.xlabel(xlabel=bidi_text1,fontsize=25,labelpad=30)
plt.yticks(ticks=np.arange(0,30,1),fontsize=15)
plt.xticks(fontsize=10)
plt.ylabel(ylabel=bidi_text2,fontsize=25,labelpad=30)
plt.title(label=bidi_text,fontsize=50,pad=30)
plt.show()