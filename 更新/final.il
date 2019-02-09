    IL_0191:  ldarg.0
    IL_0192:  ldfld      int32 Doneventscript_dlc1::number
    IL_0197:  ldc.i4.1
    IL_0198:  bne.un     IL_01cd

    IL_019d:  ldarg.0
    IL_019e:  ldfld      class [UnityEngine.TextRenderingModule]UnityEngine.TextMesh Doneventscript_dlc1::answer
    IL_01a3:  ldarg.0
    IL_01a4:  ldstr      "只有来自朝鲜、越南、古巴、罗马尼亚、老挝、柬埔寨、也门人民民主共和国、尼加拉瓜、伊朗和伊拉克的真正的马克思列宁主义政党的领导人和特使才能从国外进入地拉那。除了来自菲德尔·卡斯特罗、尼古拉·齐奥塞斯库和金日成的哀悼外，包括苏联、意大利和南斯拉夫在内的其他国家的哀悼电报都被打回。告别霍查的仪式在地拉那的斯大林宫中举行。"
                           IL_01a9:  ldc.i4.s   52
    IL_01ab:  call       instance string Doneventscript_dlc1::Text(string,
                               int32)
    IL_01b0:  callvirt   instance void [UnityEngine.TextRenderingModule]UnityEngine.TextMesh::set_text(string)
    IL_01b5:  ldarg.0
    IL_01b6:  ldfld      class global_dlc1 Doneventscript_dlc1::global1
    IL_01bb:  dup
    IL_01bc:  ldfld      int32 global_dlc1::line
    IL_01c1:  ldc.i4.1
    IL_01c2:  sub