author: Valisha Shah (Valisha) output: md\_document: variant: gfm \_\_\_

Methods
=======

-   buildIndex.sh script is to build a salmon index from the de-novo
    transcriptome
-   alignAll.sh script is to align the Aip samples according to the
    Aipindex using Salmon
-   mergeKo.R script will merge the aligned transcripts to their genes
-   de.R script is to import the Salmon alignments into DESeq2 and
    perfrom differential expression analysis, and also splitting them on
    the basis of their padg value

Results
=======

<table>
<thead>
<tr class="header">
<th></th>
<th>trans</th>
<th>ko</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>TRINITY_DN9495_c0_g1_i2</td>
<td>ko:K00134</td>
</tr>
<tr class="even">
<td>2</td>
<td>TRINITY_DN9573_c0_g1_i1</td>
<td>ko:K01689</td>
</tr>
<tr class="odd">
<td>3</td>
<td>TRINITY_DN9485_c0_g1_i1</td>
<td>ko:K02111</td>
</tr>
<tr class="even">
<td>4</td>
<td>TRINITY_DN8020_c0_g1_i1</td>
<td>ko:K04043</td>
</tr>
<tr class="odd">
<td>5</td>
<td>TRINITY_DN9453_c0_g1_i1</td>
<td>ko:K02932</td>
</tr>
<tr class="even">
<td>6</td>
<td>TRINITY_DN8136_c0_g1_i1</td>
<td>ko:K02932</td>
</tr>
<tr class="odd">
<td>7</td>
<td>TRINITY_DN9071_c0_g1_i1</td>
<td>ko:K02955</td>
</tr>
<tr class="even">
<td>8</td>
<td>TRINITY_DN9071_c0_g1_i2</td>
<td>ko:K02955</td>
</tr>
<tr class="odd">
<td>9</td>
<td>TRINITY_DN4420_c0_g1_i1</td>
<td>ko:K02923</td>
</tr>
<tr class="even">
<td>10</td>
<td>TRINITY_DN12145_c0_g1_i1</td>
<td>ko:K12165</td>
</tr>
<tr class="odd">
<td>11</td>
<td>TRINITY_DN9627_c0_g1_i1</td>
<td>ko:K01379</td>
</tr>
<tr class="even">
<td>12</td>
<td>TRINITY_DN9627_c0_g1_i2</td>
<td>ko:K01379</td>
</tr>
<tr class="odd">
<td>13</td>
<td>TRINITY_DN19319_c0_g1_i1</td>
<td>ko:K12162</td>
</tr>
<tr class="even">
<td>14</td>
<td>TRINITY_DN6099_c0_g1_i1</td>
<td>ko:K02910</td>
</tr>
<tr class="odd">
<td>15</td>
<td>TRINITY_DN8511_c0_g1_i1</td>
<td>ko:K16197</td>
</tr>
<tr class="even">
<td>16</td>
<td>TRINITY_DN7767_c0_g1_i1</td>
<td>ko:K16197</td>
</tr>
<tr class="odd">
<td>17</td>
<td>TRINITY_DN9134_c0_g2_i1</td>
<td>ko:K16197</td>
</tr>
<tr class="even">
<td>18</td>
<td>TRINITY_DN9134_c0_g1_i2</td>
<td>ko:K16197</td>
</tr>
<tr class="odd">
<td>19</td>
<td>TRINITY_DN9134_c0_g1_i3</td>
<td>ko:K16197</td>
</tr>
<tr class="even">
<td>20</td>
<td>TRINITY_DN9093_c0_g1_i1</td>
<td>ko:K16197</td>
</tr>
<tr class="odd">
<td>21</td>
<td>TRINITY_DN9134_c0_g2_i2</td>
<td>ko:K16197</td>
</tr>
<tr class="even">
<td>22</td>
<td>TRINITY_DN8733_c0_g1_i1</td>
<td>ko:K00140</td>
</tr>
<tr class="odd">
<td>23</td>
<td>TRINITY_DN8854_c0_g1_i1</td>
<td>ko:K02998</td>
</tr>
<tr class="even">
<td>24</td>
<td>TRINITY_DN4546_c0_g1_i1</td>
<td>ko:K02883</td>
</tr>
<tr class="odd">
<td>25</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K04393</td>
</tr>
<tr class="even">
<td>26</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K04393</td>
</tr>
<tr class="odd">
<td>27</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K04393</td>
</tr>
<tr class="even">
<td>28</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K04393</td>
</tr>
<tr class="odd">
<td>29</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K05692</td>
</tr>
<tr class="even">
<td>30</td>
<td>TRINITY_DN8737_c0_g1_i1</td>
<td>ko:K02155</td>
</tr>
<tr class="odd">
<td>31</td>
<td>TRINITY_DN8253_c0_g1_i1</td>
<td>ko:K02880</td>
</tr>
<tr class="even">
<td>32</td>
<td>TRINITY_DN9343_c0_g1_i1</td>
<td>ko:K01647</td>
</tr>
<tr class="odd">
<td>33</td>
<td>TRINITY_DN7331_c0_g1_i1</td>
<td>ko:K00772</td>
</tr>
<tr class="even">
<td>34</td>
<td>TRINITY_DN9525_c0_g1_i1</td>
<td>ko:K02105</td>
</tr>
<tr class="odd">
<td>35</td>
<td>TRINITY_DN9241_c0_g1_i1</td>
<td>ko:K00939</td>
</tr>
<tr class="even">
<td>36</td>
<td>TRINITY_DN7723_c0_g1_i1</td>
<td>ko:K03246</td>
</tr>
<tr class="odd">
<td>37</td>
<td>TRINITY_DN7723_c0_g2_i1</td>
<td>ko:K03246</td>
</tr>
<tr class="even">
<td>38</td>
<td>TRINITY_DN9087_c0_g1_i1</td>
<td>ko:K02984</td>
</tr>
<tr class="odd">
<td>39</td>
<td>TRINITY_DN8759_c0_g1_i1</td>
<td>ko:K13758</td>
</tr>
<tr class="even">
<td>40</td>
<td>TRINITY_DN9320_c0_g2_i2</td>
<td>ko:K02960</td>
</tr>
<tr class="odd">
<td>41</td>
<td>TRINITY_DN9320_c0_g2_i1</td>
<td>ko:K02960</td>
</tr>
<tr class="even">
<td>42</td>
<td>TRINITY_DN6283_c0_g1_i1</td>
<td>ko:K02894</td>
</tr>
<tr class="odd">
<td>46</td>
<td>TRINITY_DN7353_c0_g1_i1</td>
<td>ko:K00331</td>
</tr>
<tr class="even">
<td>47</td>
<td>TRINITY_DN9267_c0_g1_i2</td>
<td>ko:K00024</td>
</tr>
<tr class="odd">
<td>48</td>
<td>TRINITY_DN9611_c0_g2_i1</td>
<td>ko:K01596</td>
</tr>
<tr class="even">
<td>49</td>
<td>TRINITY_DN9611_c0_g2_i2</td>
<td>ko:K01596</td>
</tr>
<tr class="odd">
<td>51</td>
<td>TRINITY_DN9596_c0_g1_i1</td>
<td>ko:K02112</td>
</tr>
<tr class="even">
<td>52</td>
<td>TRINITY_DN9562_c0_g1_i1</td>
<td>ko:K00789</td>
</tr>
<tr class="odd">
<td>55</td>
<td>TRINITY_DN6874_c0_g1_i1</td>
<td>ko:K00333</td>
</tr>
<tr class="even">
<td>56</td>
<td>TRINITY_DN6548_c0_g1_i1</td>
<td>ko:K00338</td>
</tr>
<tr class="odd">
<td>58</td>
<td>TRINITY_DN9231_c0_g1_i1</td>
<td>ko:K01251</td>
</tr>
<tr class="even">
<td>69</td>
<td>TRINITY_DN5432_c0_g1_i1</td>
<td>ko:K03094</td>
</tr>
<tr class="odd">
<td>71</td>
<td>TRINITY_DN21870_c0_g1_i1</td>
<td>ko:K02914</td>
</tr>
<tr class="even">
<td>109</td>
<td>TRINITY_DN2488_c0_g1_i1</td>
<td>ko:K01724</td>
</tr>
<tr class="odd">
<td>118</td>
<td>TRINITY_DN9429_c0_g1_i1</td>
<td>ko:K13025</td>
</tr>
<tr class="even">
<td>119</td>
<td>TRINITY_DN7983_c0_g1_i1</td>
<td>ko:K13025</td>
</tr>
<tr class="odd">
<td>120</td>
<td>TRINITY_DN8592_c0_g1_i1</td>
<td>ko:K11251</td>
</tr>
<tr class="even">
<td>123</td>
<td>TRINITY_DN4628_c0_g1_i1</td>
<td>ko:K07953</td>
</tr>
<tr class="odd">
<td>124</td>
<td>TRINITY_DN9165_c0_g1_i2</td>
<td>ko:K11252</td>
</tr>
<tr class="even">
<td>125</td>
<td>TRINITY_DN15080_c0_g1_i1</td>
<td>ko:K11252</td>
</tr>
<tr class="odd">
<td>126</td>
<td>TRINITY_DN9165_c0_g1_i1</td>
<td>ko:K11252</td>
</tr>
<tr class="even">
<td>127</td>
<td>TRINITY_DN9429_c0_g1_i1</td>
<td>ko:K03257</td>
</tr>
<tr class="odd">
<td>128</td>
<td>TRINITY_DN7983_c0_g1_i1</td>
<td>ko:K03257</td>
</tr>
<tr class="even">
<td>130</td>
<td>TRINITY_DN9626_c0_g1_i1</td>
<td>ko:K12823</td>
</tr>
<tr class="odd">
<td>131</td>
<td>TRINITY_DN19396_c0_g1_i1</td>
<td>ko:K12625</td>
</tr>
<tr class="even">
<td>132</td>
<td>TRINITY_DN9075_c0_g1_i2</td>
<td>ko:K12812</td>
</tr>
<tr class="odd">
<td>133</td>
<td>TRINITY_DN9075_c0_g1_i3</td>
<td>ko:K12812</td>
</tr>
<tr class="even">
<td>150</td>
<td>TRINITY_DN8143_c2_g1_i1</td>
<td>ko:K06215</td>
</tr>
<tr class="odd">
<td>155</td>
<td>TRINITY_DN9481_c3_g1_i6</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>156</td>
<td>TRINITY_DN9481_c3_g1_i15</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>157</td>
<td>TRINITY_DN9481_c3_g1_i11</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>158</td>
<td>TRINITY_DN9481_c3_g1_i5</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>159</td>
<td>TRINITY_DN9481_c3_g1_i12</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>160</td>
<td>TRINITY_DN9481_c3_g1_i7</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>161</td>
<td>TRINITY_DN9481_c3_g1_i10</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>162</td>
<td>TRINITY_DN9481_c3_g1_i3</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>163</td>
<td>TRINITY_DN9481_c3_g1_i8</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>164</td>
<td>TRINITY_DN9234_c0_g1_i1</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>165</td>
<td>TRINITY_DN9481_c3_g1_i14</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>166</td>
<td>TRINITY_DN9481_c3_g1_i13</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>167</td>
<td>TRINITY_DN9481_c3_g1_i2</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>168</td>
<td>TRINITY_DN9481_c3_g1_i16</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>169</td>
<td>TRINITY_DN9481_c3_g1_i1</td>
<td>ko:K08341</td>
</tr>
<tr class="even">
<td>170</td>
<td>TRINITY_DN9481_c3_g1_i9</td>
<td>ko:K08341</td>
</tr>
<tr class="odd">
<td>171</td>
<td>TRINITY_DN7764_c0_g1_i1</td>
<td>ko:K02973</td>
</tr>
<tr class="even">
<td>172</td>
<td>TRINITY_DN7532_c0_g1_i1</td>
<td>ko:K11827</td>
</tr>
<tr class="odd">
<td>174</td>
<td>TRINITY_DN9469_c0_g2_i1</td>
<td>ko:K02925</td>
</tr>
<tr class="even">
<td>178</td>
<td>TRINITY_DN8250_c0_g1_i1</td>
<td>ko:K11251</td>
</tr>
<tr class="odd">
<td>179</td>
<td>TRINITY_DN7867_c0_g1_i1</td>
<td>ko:K11251</td>
</tr>
<tr class="even">
<td>180</td>
<td>TRINITY_DN25720_c0_g1_i1</td>
<td>ko:K11251</td>
</tr>
<tr class="odd">
<td>184</td>
<td>TRINITY_DN3357_c0_g1_i1</td>
<td>ko:K09568</td>
</tr>
<tr class="even">
<td>185</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K03768</td>
</tr>
<tr class="odd">
<td>189</td>
<td>TRINITY_DN10058_c0_g1_i1</td>
<td>ko:K10752</td>
</tr>
<tr class="even">
<td>190</td>
<td>TRINITY_DN561_c0_g1_i1</td>
<td>ko:K00940</td>
</tr>
<tr class="odd">
<td>191</td>
<td>TRINITY_DN8388_c0_g1_i1</td>
<td>ko:K00940</td>
</tr>
<tr class="even">
<td>194</td>
<td>TRINITY_DN7930_c0_g1_i1</td>
<td>ko:K04565</td>
</tr>
<tr class="odd">
<td>197</td>
<td>TRINITY_DN9341_c0_g1_i1</td>
<td>ko:K08967</td>
</tr>
<tr class="even">
<td>201</td>
<td>TRINITY_DN6990_c0_g1_i1</td>
<td>ko:K09568</td>
</tr>
<tr class="odd">
<td>202</td>
<td>TRINITY_DN8301_c0_g1_i1</td>
<td>ko:K10573</td>
</tr>
<tr class="even">
<td>203</td>
<td>TRINITY_DN1082_c0_g1_i1</td>
<td>ko:K07375</td>
</tr>
<tr class="odd">
<td>204</td>
<td>TRINITY_DN8706_c0_g1_i1</td>
<td>ko:K07375</td>
</tr>
<tr class="even">
<td>205</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K09567</td>
</tr>
<tr class="odd">
<td>206</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K09567</td>
</tr>
<tr class="even">
<td>213</td>
<td>TRINITY_DN9609_c0_g1_i1</td>
<td>ko:K03231</td>
</tr>
<tr class="odd">
<td>214</td>
<td>TRINITY_DN7764_c0_g1_i1</td>
<td>ko:K02950</td>
</tr>
<tr class="even">
<td>215</td>
<td>TRINITY_DN6283_c0_g1_i1</td>
<td>ko:K02874</td>
</tr>
<tr class="odd">
<td>216</td>
<td>TRINITY_DN9071_c0_g1_i2</td>
<td>ko:K02948</td>
</tr>
<tr class="even">
<td>217</td>
<td>TRINITY_DN9071_c0_g1_i1</td>
<td>ko:K02948</td>
</tr>
<tr class="odd">
<td>230</td>
<td>TRINITY_DN19535_c0_g1_i1</td>
<td>ko:K05863</td>
</tr>
<tr class="even">
<td>237</td>
<td>TRINITY_DN9379_c3_g1_i2</td>
<td>ko:K17286</td>
</tr>
<tr class="odd">
<td>238</td>
<td>TRINITY_DN9379_c3_g1_i6</td>
<td>ko:K17286</td>
</tr>
<tr class="even">
<td>239</td>
<td>TRINITY_DN9379_c3_g1_i4</td>
<td>ko:K17286</td>
</tr>
<tr class="odd">
<td>240</td>
<td>TRINITY_DN9379_c3_g1_i5</td>
<td>ko:K17286</td>
</tr>
<tr class="even">
<td>241</td>
<td>TRINITY_DN9379_c3_g1_i1</td>
<td>ko:K17286</td>
</tr>
<tr class="odd">
<td>242</td>
<td>TRINITY_DN9379_c3_g1_i3</td>
<td>ko:K17286</td>
</tr>
<tr class="even">
<td>243</td>
<td>TRINITY_DN9098_c0_g1_i1</td>
<td>ko:K02962</td>
</tr>
<tr class="odd">
<td>244</td>
<td>TRINITY_DN7188_c0_g1_i1</td>
<td>ko:K02877</td>
</tr>
<tr class="even">
<td>246</td>
<td>TRINITY_DN2396_c0_g1_i1</td>
<td>ko:K02938</td>
</tr>
<tr class="odd">
<td>247</td>
<td>TRINITY_DN14986_c0_g1_i1</td>
<td>ko:K02953</td>
</tr>
<tr class="even">
<td>248</td>
<td>TRINITY_DN8391_c0_g1_i1</td>
<td>ko:K02953</td>
</tr>
<tr class="odd">
<td>249</td>
<td>TRINITY_DN8757_c0_g1_i1</td>
<td>ko:K02936</td>
</tr>
<tr class="even">
<td>250</td>
<td>TRINITY_DN8110_c0_g1_i1</td>
<td>ko:K03113</td>
</tr>
<tr class="odd">
<td>253</td>
<td>TRINITY_DN5342_c0_g2_i1</td>
<td>ko:K05863</td>
</tr>
<tr class="even">
<td>260</td>
<td>TRINITY_DN7982_c0_g1_i1</td>
<td>ko:K05758</td>
</tr>
<tr class="odd">
<td>261</td>
<td>TRINITY_DN7982_c0_g2_i1</td>
<td>ko:K05758</td>
</tr>
<tr class="even">
<td>262</td>
<td>TRINITY_DN2486_c1_g1_i1</td>
<td>ko:K03008</td>
</tr>
<tr class="odd">
<td>263</td>
<td>TRINITY_DN8718_c0_g1_i1</td>
<td>ko:K02949</td>
</tr>
<tr class="even">
<td>265</td>
<td>TRINITY_DN8486_c0_g1_i1</td>
<td>ko:K02993</td>
</tr>
<tr class="odd">
<td>268</td>
<td>TRINITY_DN8677_c0_g1_i1</td>
<td>ko:K02976</td>
</tr>
<tr class="even">
<td>269</td>
<td>TRINITY_DN13091_c0_g1_i1</td>
<td>ko:K11252</td>
</tr>
<tr class="odd">
<td>289</td>
<td>TRINITY_DN7097_c0_g2_i1</td>
<td>ko:K03635</td>
</tr>
<tr class="even">
<td>290</td>
<td>TRINITY_DN7097_c0_g1_i1</td>
<td>ko:K03635</td>
</tr>
<tr class="odd">
<td>291</td>
<td>TRINITY_DN25050_c0_g1_i1</td>
<td>ko:K02256</td>
</tr>
<tr class="even">
<td>292</td>
<td>TRINITY_DN25050_c0_g1_i1</td>
<td>ko:K02262</td>
</tr>
<tr class="odd">
<td>294</td>
<td>TRINITY_DN9405_c0_g1_i1</td>
<td>ko:K03283</td>
</tr>
<tr class="even">
<td>295</td>
<td>TRINITY_DN9405_c0_g1_i2</td>
<td>ko:K03283</td>
</tr>
<tr class="odd">
<td>298</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K04513</td>
</tr>
<tr class="even">
<td>301</td>
<td>TRINITY_DN9363_c0_g1_i1</td>
<td>ko:K00235</td>
</tr>
<tr class="odd">
<td>302</td>
<td>TRINITY_DN9405_c0_g1_i1</td>
<td>ko:K09490</td>
</tr>
<tr class="even">
<td>303</td>
<td>TRINITY_DN9405_c0_g1_i2</td>
<td>ko:K09490</td>
</tr>
<tr class="odd">
<td>304</td>
<td>TRINITY_DN9310_c0_g1_i1</td>
<td>ko:K22068</td>
</tr>
<tr class="even">
<td>305</td>
<td>TRINITY_DN6976_c0_g2_i1</td>
<td>ko:K03007</td>
</tr>
<tr class="odd">
<td>306</td>
<td>TRINITY_DN6976_c0_g1_i1</td>
<td>ko:K03007</td>
</tr>
<tr class="even">
<td>307</td>
<td>TRINITY_DN9431_c1_g1_i1</td>
<td>ko:K01915</td>
</tr>
<tr class="odd">
<td>310</td>
<td>TRINITY_DN11213_c0_g1_i1</td>
<td>ko:K02971</td>
</tr>
<tr class="even">
<td>312</td>
<td>TRINITY_DN579_c0_g1_i1</td>
<td>ko:K11254</td>
</tr>
<tr class="odd">
<td>314</td>
<td>TRINITY_DN4609_c0_g2_i1</td>
<td>ko:K12859</td>
</tr>
<tr class="even">
<td>315</td>
<td>TRINITY_DN4609_c0_g1_i1</td>
<td>ko:K12859</td>
</tr>
<tr class="odd">
<td>317</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07937</td>
</tr>
<tr class="even">
<td>318</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="odd">
<td>319</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="even">
<td>320</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="odd">
<td>321</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="even">
<td>322</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="odd">
<td>323</td>
<td>TRINITY_DN14631_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="even">
<td>336</td>
<td>TRINITY_DN8794_c0_g1_i1</td>
<td>ko:K12845</td>
</tr>
<tr class="odd">
<td>337</td>
<td>TRINITY_DN6006_c0_g1_i1</td>
<td>ko:K02924</td>
</tr>
<tr class="even">
<td>338</td>
<td>TRINITY_DN5817_c0_g1_i1</td>
<td>ko:K02957</td>
</tr>
<tr class="odd">
<td>339</td>
<td>TRINITY_DN8919_c0_g1_i1</td>
<td>ko:K02868</td>
</tr>
<tr class="even">
<td>341</td>
<td>TRINITY_DN9495_c0_g1_i1</td>
<td>ko:K00134</td>
</tr>
<tr class="odd">
<td>343</td>
<td>TRINITY_DN8210_c0_g1_i2</td>
<td>ko:K02980</td>
</tr>
<tr class="even">
<td>344</td>
<td>TRINITY_DN8210_c0_g1_i1</td>
<td>ko:K02980</td>
</tr>
<tr class="odd">
<td>347</td>
<td>TRINITY_DN23350_c0_g1_i1</td>
<td>ko:K13113</td>
</tr>
<tr class="even">
<td>368</td>
<td>TRINITY_DN7549_c0_g1_i1</td>
<td>ko:K02937</td>
</tr>
<tr class="odd">
<td>370</td>
<td>TRINITY_DN7617_c0_g1_i1</td>
<td>ko:K02865</td>
</tr>
<tr class="even">
<td>372</td>
<td>TRINITY_DN8062_c0_g1_i1</td>
<td>ko:K02929</td>
</tr>
<tr class="odd">
<td>373</td>
<td>TRINITY_DN8062_c0_g2_i1</td>
<td>ko:K02929</td>
</tr>
<tr class="even">
<td>374</td>
<td>TRINITY_DN8062_c0_g3_i1</td>
<td>ko:K02929</td>
</tr>
<tr class="odd">
<td>375</td>
<td>TRINITY_DN9164_c0_g1_i1</td>
<td>ko:K03234</td>
</tr>
<tr class="even">
<td>376</td>
<td>TRINITY_DN8950_c0_g1_i1</td>
<td>ko:K08738</td>
</tr>
<tr class="odd">
<td>377</td>
<td>TRINITY_DN9128_c0_g1_i2</td>
<td>ko:K07374</td>
</tr>
<tr class="even">
<td>378</td>
<td>TRINITY_DN18948_c0_g1_i1</td>
<td>ko:K02908</td>
</tr>
<tr class="odd">
<td>379</td>
<td>TRINITY_DN18948_c0_g2_i1</td>
<td>ko:K02908</td>
</tr>
<tr class="even">
<td>380</td>
<td>TRINITY_DN8915_c0_g1_i1</td>
<td>ko:K02908</td>
</tr>
<tr class="odd">
<td>382</td>
<td>TRINITY_DN9419_c0_g1_i1</td>
<td>ko:K10956</td>
</tr>
<tr class="even">
<td>388</td>
<td>TRINITY_DN24339_c0_g1_i1</td>
<td>ko:K01803</td>
</tr>
<tr class="odd">
<td>389</td>
<td>TRINITY_DN7796_c0_g1_i1</td>
<td>ko:K02912</td>
</tr>
<tr class="even">
<td>390</td>
<td>TRINITY_DN7667_c0_g1_i1</td>
<td>ko:K02921</td>
</tr>
<tr class="odd">
<td>392</td>
<td>TRINITY_DN8872_c0_g2_i1</td>
<td>ko:K15423</td>
</tr>
<tr class="even">
<td>400</td>
<td>TRINITY_DN8801_c0_g1_i1</td>
<td>ko:K02991</td>
</tr>
<tr class="odd">
<td>401</td>
<td>TRINITY_DN1554_c0_g1_i1</td>
<td>ko:K02979</td>
</tr>
<tr class="even">
<td>402</td>
<td>TRINITY_DN8695_c0_g1_i1</td>
<td>ko:K07936</td>
</tr>
<tr class="odd">
<td>403</td>
<td>TRINITY_DN1716_c0_g1_i1</td>
<td>ko:K11130</td>
</tr>
<tr class="even">
<td>404</td>
<td>TRINITY_DN9446_c0_g1_i1</td>
<td>ko:K00024</td>
</tr>
<tr class="odd">
<td>437</td>
<td>TRINITY_DN8406_c0_g1_i1</td>
<td>ko:K02995</td>
</tr>
<tr class="even">
<td>442</td>
<td>TRINITY_DN7637_c0_g1_i1</td>
<td>ko:K02898</td>
</tr>
<tr class="odd">
<td>443</td>
<td>TRINITY_DN24979_c0_g1_i1</td>
<td>ko:K02703</td>
</tr>
<tr class="even">
<td>445</td>
<td>TRINITY_DN7881_c0_g1_i1</td>
<td>ko:K02706</td>
</tr>
<tr class="odd">
<td>452</td>
<td>TRINITY_DN1635_c0_g1_i1</td>
<td>ko:K02635</td>
</tr>
<tr class="even">
<td>461</td>
<td>TRINITY_DN4429_c0_g1_i1</td>
<td>ko:K02704</td>
</tr>
<tr class="odd">
<td>494</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K07827</td>
</tr>
<tr class="even">
<td>495</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K07827</td>
</tr>
<tr class="odd">
<td>497</td>
<td>TRINITY_DN9613_c0_g1_i3</td>
<td>ko:K10365</td>
</tr>
<tr class="even">
<td>499</td>
<td>TRINITY_DN9025_c0_g2_i1</td>
<td>ko:K06269</td>
</tr>
<tr class="odd">
<td>500</td>
<td>TRINITY_DN8516_c1_g2_i1</td>
<td>ko:K06269</td>
</tr>
<tr class="even">
<td>502</td>
<td>TRINITY_DN8070_c0_g1_i4</td>
<td>ko:K10418</td>
</tr>
<tr class="odd">
<td>503</td>
<td>TRINITY_DN8070_c0_g1_i1</td>
<td>ko:K10418</td>
</tr>
<tr class="even">
<td>504</td>
<td>TRINITY_DN8070_c0_g1_i3</td>
<td>ko:K10418</td>
</tr>
<tr class="odd">
<td>505</td>
<td>TRINITY_DN8070_c0_g1_i2</td>
<td>ko:K10418</td>
</tr>
<tr class="even">
<td>506</td>
<td>TRINITY_DN9333_c0_g1_i1</td>
<td>ko:K00128</td>
</tr>
<tr class="odd">
<td>507</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04630</td>
</tr>
<tr class="even">
<td>509</td>
<td>TRINITY_DN6396_c0_g1_i1</td>
<td>ko:K11253</td>
</tr>
<tr class="odd">
<td>513</td>
<td>TRINITY_DN7877_c0_g1_i1</td>
<td>ko:K02183</td>
</tr>
<tr class="even">
<td>514</td>
<td>TRINITY_DN9426_c0_g1_i1</td>
<td>ko:K02183</td>
</tr>
<tr class="odd">
<td>515</td>
<td>TRINITY_DN9151_c0_g1_i1</td>
<td>ko:K02183</td>
</tr>
<tr class="even">
<td>528</td>
<td>TRINITY_DN8258_c0_g1_i1</td>
<td>ko:K02966</td>
</tr>
<tr class="odd">
<td>530</td>
<td>TRINITY_DN9017_c0_g1_i2</td>
<td>ko:K00262</td>
</tr>
<tr class="even">
<td>531</td>
<td>TRINITY_DN9017_c0_g1_i1</td>
<td>ko:K00262</td>
</tr>
<tr class="odd">
<td>533</td>
<td>TRINITY_DN4552_c0_g2_i1</td>
<td>ko:K02922</td>
</tr>
<tr class="even">
<td>534</td>
<td>TRINITY_DN4552_c0_g1_i1</td>
<td>ko:K02922</td>
</tr>
<tr class="odd">
<td>554</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K04513</td>
</tr>
<tr class="even">
<td>555</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K04513</td>
</tr>
<tr class="odd">
<td>557</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K04513</td>
</tr>
<tr class="even">
<td>562</td>
<td>TRINITY_DN8872_c0_g2_i1</td>
<td>ko:K04382</td>
</tr>
<tr class="odd">
<td>629</td>
<td>TRINITY_DN2396_c0_g1_i1</td>
<td>ko:K02886</td>
</tr>
<tr class="even">
<td>633</td>
<td>TRINITY_DN7340_c0_g1_i1</td>
<td>ko:K02992</td>
</tr>
<tr class="odd">
<td>674</td>
<td>TRINITY_DN13269_c0_g1_i1</td>
<td>ko:K02713</td>
</tr>
<tr class="even">
<td>677</td>
<td>TRINITY_DN6874_c0_g1_i1</td>
<td>ko:K03935</td>
</tr>
<tr class="odd">
<td>679</td>
<td>TRINITY_DN9485_c0_g1_i1</td>
<td>ko:K02132</td>
</tr>
<tr class="even">
<td>681</td>
<td>TRINITY_DN3888_c0_g1_i1</td>
<td>ko:K12734</td>
</tr>
<tr class="odd">
<td>682</td>
<td>TRINITY_DN8231_c0_g1_i2</td>
<td>ko:K07874</td>
</tr>
<tr class="even">
<td>683</td>
<td>TRINITY_DN9575_c3_g1_i1</td>
<td>ko:K07874</td>
</tr>
<tr class="odd">
<td>684</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K07874</td>
</tr>
<tr class="even">
<td>685</td>
<td>TRINITY_DN8231_c0_g1_i1</td>
<td>ko:K07874</td>
</tr>
<tr class="odd">
<td>686</td>
<td>TRINITY_DN8980_c0_g1_i1</td>
<td>ko:K12877</td>
</tr>
<tr class="even">
<td>687</td>
<td>TRINITY_DN8980_c0_g1_i2</td>
<td>ko:K12877</td>
</tr>
<tr class="odd">
<td>689</td>
<td>TRINITY_DN8670_c0_g1_i1</td>
<td>ko:K02885</td>
</tr>
<tr class="even">
<td>690</td>
<td>TRINITY_DN8934_c0_g1_i1</td>
<td>ko:K02958</td>
</tr>
<tr class="odd">
<td>691</td>
<td>TRINITY_DN9267_c0_g1_i2</td>
<td>ko:K00025</td>
</tr>
<tr class="even">
<td>693</td>
<td>TRINITY_DN9655_c0_g5_i7</td>
<td>ko:K07374</td>
</tr>
<tr class="odd">
<td>695</td>
<td>TRINITY_DN7248_c0_g1_i1</td>
<td>ko:K02917</td>
</tr>
<tr class="even">
<td>696</td>
<td>TRINITY_DN7720_c0_g1_i1</td>
<td>ko:K04802</td>
</tr>
<tr class="odd">
<td>710</td>
<td>TRINITY_DN957_c0_g1_i1</td>
<td>ko:K03065</td>
</tr>
<tr class="even">
<td>712</td>
<td>TRINITY_DN9575_c3_g1_i1</td>
<td>ko:K07904</td>
</tr>
<tr class="odd">
<td>713</td>
<td>TRINITY_DN8336_c0_g1_i1</td>
<td>ko:K03083</td>
</tr>
<tr class="even">
<td>717</td>
<td>TRINITY_DN2123_c0_g1_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>718</td>
<td>TRINITY_DN8993_c1_g1_i10</td>
<td>ko:K12158</td>
</tr>
<tr class="even">
<td>719</td>
<td>TRINITY_DN2123_c0_g2_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>720</td>
<td>TRINITY_DN8268_c0_g1_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="even">
<td>721</td>
<td>TRINITY_DN937_c0_g1_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>722</td>
<td>TRINITY_DN8993_c1_g1_i11</td>
<td>ko:K12158</td>
</tr>
<tr class="even">
<td>723</td>
<td>TRINITY_DN16207_c0_g1_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>724</td>
<td>TRINITY_DN8993_c1_g1_i2</td>
<td>ko:K12158</td>
</tr>
<tr class="even">
<td>727</td>
<td>TRINITY_DN8993_c1_g1_i5</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>728</td>
<td>TRINITY_DN8993_c1_g1_i4</td>
<td>ko:K12158</td>
</tr>
<tr class="even">
<td>729</td>
<td>TRINITY_DN1595_c0_g1_i1</td>
<td>ko:K02900</td>
</tr>
<tr class="odd">
<td>730</td>
<td>TRINITY_DN9357_c0_g2_i2</td>
<td>ko:K18584</td>
</tr>
<tr class="even">
<td>731</td>
<td>TRINITY_DN9357_c0_g2_i3</td>
<td>ko:K18584</td>
</tr>
<tr class="odd">
<td>735</td>
<td>TRINITY_DN8960_c0_g1_i1</td>
<td>ko:K03263</td>
</tr>
<tr class="even">
<td>736</td>
<td>TRINITY_DN7313_c0_g1_i1</td>
<td>ko:K02866</td>
</tr>
<tr class="odd">
<td>744</td>
<td>TRINITY_DN6781_c0_g2_i1</td>
<td>ko:K02726</td>
</tr>
<tr class="even">
<td>745</td>
<td>TRINITY_DN6781_c0_g1_i1</td>
<td>ko:K02726</td>
</tr>
<tr class="odd">
<td>746</td>
<td>TRINITY_DN6781_c0_g3_i1</td>
<td>ko:K02726</td>
</tr>
<tr class="even">
<td>747</td>
<td>TRINITY_DN6548_c0_g1_i1</td>
<td>ko:K03941</td>
</tr>
<tr class="odd">
<td>748</td>
<td>TRINITY_DN8852_c0_g1_i2</td>
<td>ko:K10580</td>
</tr>
<tr class="even">
<td>749</td>
<td>TRINITY_DN8852_c0_g1_i1</td>
<td>ko:K10580</td>
</tr>
<tr class="odd">
<td>751</td>
<td>TRINITY_DN9544_c0_g1_i1</td>
<td>ko:K14753</td>
</tr>
<tr class="even">
<td>756</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K04392</td>
</tr>
<tr class="odd">
<td>757</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K04392</td>
</tr>
<tr class="even">
<td>759</td>
<td>TRINITY_DN24479_c0_g1_i1</td>
<td>ko:K12622</td>
</tr>
<tr class="odd">
<td>760</td>
<td>TRINITY_DN9134_c0_g1_i3</td>
<td>ko:K06630</td>
</tr>
<tr class="even">
<td>761</td>
<td>TRINITY_DN7767_c0_g1_i1</td>
<td>ko:K06630</td>
</tr>
<tr class="odd">
<td>762</td>
<td>TRINITY_DN9134_c0_g2_i2</td>
<td>ko:K06630</td>
</tr>
<tr class="even">
<td>763</td>
<td>TRINITY_DN9134_c0_g2_i1</td>
<td>ko:K06630</td>
</tr>
<tr class="odd">
<td>764</td>
<td>TRINITY_DN8511_c0_g1_i1</td>
<td>ko:K06630</td>
</tr>
<tr class="even">
<td>765</td>
<td>TRINITY_DN9134_c0_g1_i2</td>
<td>ko:K06630</td>
</tr>
<tr class="odd">
<td>766</td>
<td>TRINITY_DN9451_c0_g1_i1</td>
<td>ko:K07897</td>
</tr>
<tr class="even">
<td>767</td>
<td>TRINITY_DN6457_c0_g1_i1</td>
<td>ko:K02964</td>
</tr>
<tr class="odd">
<td>770</td>
<td>TRINITY_DN937_c0_g1_i1</td>
<td>ko:K02977</td>
</tr>
<tr class="even">
<td>783</td>
<td>TRINITY_DN9575_c3_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="odd">
<td>792</td>
<td>TRINITY_DN5329_c0_g1_i1</td>
<td>ko:K12668</td>
</tr>
<tr class="even">
<td>793</td>
<td>TRINITY_DN24935_c0_g1_i1</td>
<td>ko:K02940</td>
</tr>
<tr class="odd">
<td>796</td>
<td>TRINITY_DN8533_c0_g1_i2</td>
<td>ko:K07151</td>
</tr>
<tr class="even">
<td>797</td>
<td>TRINITY_DN8533_c0_g1_i1</td>
<td>ko:K07151</td>
</tr>
<tr class="odd">
<td>813</td>
<td>TRINITY_DN2321_c0_g1_i1</td>
<td>ko:K10688</td>
</tr>
<tr class="even">
<td>815</td>
<td>TRINITY_DN9458_c1_g1_i1</td>
<td>ko:K11188</td>
</tr>
<tr class="odd">
<td>819</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K10355</td>
</tr>
<tr class="even">
<td>820</td>
<td>TRINITY_DN9451_c0_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="odd">
<td>823</td>
<td>TRINITY_DN8872_c0_g2_i1</td>
<td>ko:K15498</td>
</tr>
<tr class="even">
<td>824</td>
<td>TRINITY_DN9603_c0_g2_i1</td>
<td>ko:K06943</td>
</tr>
<tr class="odd">
<td>835</td>
<td>TRINITY_DN9446_c0_g1_i1</td>
<td>ko:K00026</td>
</tr>
<tr class="even">
<td>836</td>
<td>TRINITY_DN1084_c0_g2_i1</td>
<td>ko:K02729</td>
</tr>
<tr class="odd">
<td>837</td>
<td>TRINITY_DN1084_c0_g1_i1</td>
<td>ko:K02729</td>
</tr>
<tr class="even">
<td>840</td>
<td>TRINITY_DN9440_c0_g1_i1</td>
<td>ko:K00031</td>
</tr>
<tr class="odd">
<td>844</td>
<td>TRINITY_DN8993_c1_g1_i10</td>
<td>ko:K08770</td>
</tr>
<tr class="even">
<td>845</td>
<td>TRINITY_DN8993_c1_g1_i5</td>
<td>ko:K08770</td>
</tr>
<tr class="odd">
<td>847</td>
<td>TRINITY_DN2123_c0_g2_i1</td>
<td>ko:K08770</td>
</tr>
<tr class="even">
<td>850</td>
<td>TRINITY_DN8993_c1_g1_i4</td>
<td>ko:K08770</td>
</tr>
<tr class="odd">
<td>857</td>
<td>TRINITY_DN8776_c0_g1_i1</td>
<td>ko:K02981</td>
</tr>
<tr class="even">
<td>881</td>
<td>TRINITY_DN7177_c0_g1_i1</td>
<td>ko:K00432</td>
</tr>
<tr class="odd">
<td>883</td>
<td>TRINITY_DN1045_c0_g1_i1</td>
<td>ko:K06689</td>
</tr>
<tr class="even">
<td>884</td>
<td>TRINITY_DN14990_c0_g1_i1</td>
<td>ko:K06689</td>
</tr>
<tr class="odd">
<td>885</td>
<td>TRINITY_DN6341_c0_g1_i1</td>
<td>ko:K06689</td>
</tr>
<tr class="even">
<td>937</td>
<td>TRINITY_DN21854_c0_g1_i1</td>
<td>ko:K12626</td>
</tr>
<tr class="odd">
<td>956</td>
<td>TRINITY_DN24340_c0_g1_i1</td>
<td>ko:K02730</td>
</tr>
<tr class="even">
<td>960</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="odd">
<td>961</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07977</td>
</tr>
<tr class="even">
<td>962</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="odd">
<td>964</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K01802</td>
</tr>
<tr class="even">
<td>965</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K01802</td>
</tr>
<tr class="odd">
<td>970</td>
<td>TRINITY_DN9220_c0_g1_i1</td>
<td>ko:K02987</td>
</tr>
<tr class="even">
<td>971</td>
<td>TRINITY_DN5994_c0_g1_i1</td>
<td>ko:K12394</td>
</tr>
<tr class="odd">
<td>976</td>
<td>TRINITY_DN8698_c0_g1_i1</td>
<td>ko:K02983</td>
</tr>
<tr class="even">
<td>978</td>
<td>TRINITY_DN9301_c0_g1_i2</td>
<td>ko:K17081</td>
</tr>
<tr class="odd">
<td>982</td>
<td>TRINITY_DN7542_c0_g1_i1</td>
<td>ko:K07893</td>
</tr>
<tr class="even">
<td>984</td>
<td>TRINITY_DN6405_c0_g1_i1</td>
<td>ko:K11099</td>
</tr>
<tr class="odd">
<td>985</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07942</td>
</tr>
<tr class="even">
<td>986</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07942</td>
</tr>
<tr class="odd">
<td>987</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07942</td>
</tr>
<tr class="even">
<td>988</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07942</td>
</tr>
<tr class="odd">
<td>989</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07942</td>
</tr>
<tr class="even">
<td>995</td>
<td>TRINITY_DN762_c0_g1_i1</td>
<td>ko:K02219</td>
</tr>
<tr class="odd">
<td>1004</td>
<td>TRINITY_DN8336_c0_g1_i1</td>
<td>ko:K00924</td>
</tr>
<tr class="even">
<td>1006</td>
<td>TRINITY_DN8753_c0_g1_i1</td>
<td>ko:K02985</td>
</tr>
<tr class="odd">
<td>1008</td>
<td>TRINITY_DN8392_c0_g1_i1</td>
<td>ko:K02901</td>
</tr>
<tr class="even">
<td>1022</td>
<td>TRINITY_DN8993_c1_g1_i10</td>
<td>ko:K02927</td>
</tr>
<tr class="odd">
<td>1023</td>
<td>TRINITY_DN17244_c0_g1_i1</td>
<td>ko:K02927</td>
</tr>
<tr class="even">
<td>1025</td>
<td>TRINITY_DN8993_c1_g1_i5</td>
<td>ko:K02927</td>
</tr>
<tr class="odd">
<td>1026</td>
<td>TRINITY_DN8268_c0_g1_i1</td>
<td>ko:K02927</td>
</tr>
<tr class="even">
<td>1027</td>
<td>TRINITY_DN2123_c0_g2_i1</td>
<td>ko:K02927</td>
</tr>
<tr class="odd">
<td>1028</td>
<td>TRINITY_DN2123_c0_g1_i1</td>
<td>ko:K02927</td>
</tr>
<tr class="even">
<td>1029</td>
<td>TRINITY_DN937_c0_g1_i1</td>
<td>ko:K02927</td>
</tr>
<tr class="odd">
<td>1030</td>
<td>TRINITY_DN8993_c1_g1_i4</td>
<td>ko:K02927</td>
</tr>
<tr class="even">
<td>1031</td>
<td>TRINITY_DN8993_c1_g1_i2</td>
<td>ko:K02927</td>
</tr>
<tr class="odd">
<td>1033</td>
<td>TRINITY_DN8993_c1_g1_i11</td>
<td>ko:K02927</td>
</tr>
<tr class="even">
<td>1034</td>
<td>TRINITY_DN14208_c0_g1_i1</td>
<td>ko:K22063</td>
</tr>
<tr class="odd">
<td>1037</td>
<td>TRINITY_DN9245_c0_g1_i1</td>
<td>ko:K02870</td>
</tr>
<tr class="even">
<td>1038</td>
<td>TRINITY_DN7340_c0_g1_i1</td>
<td>ko:K02989</td>
</tr>
<tr class="odd">
<td>1045</td>
<td>TRINITY_DN5705_c0_g2_i1</td>
<td>ko:K02918</td>
</tr>
<tr class="even">
<td>1046</td>
<td>TRINITY_DN5705_c0_g1_i1</td>
<td>ko:K02918</td>
</tr>
<tr class="odd">
<td>1047</td>
<td>TRINITY_DN25646_c0_g1_i1</td>
<td>ko:K02893</td>
</tr>
<tr class="even">
<td>1054</td>
<td>TRINITY_DN546_c0_g1_i1</td>
<td>ko:K01070</td>
</tr>
<tr class="odd">
<td>1066</td>
<td>TRINITY_DN9523_c0_g1_i1</td>
<td>ko:K17255</td>
</tr>
<tr class="even">
<td>1072</td>
<td>TRINITY_DN7610_c0_g1_i1</td>
<td>ko:K02896</td>
</tr>
<tr class="odd">
<td>1089</td>
<td>TRINITY_DN8097_c0_g1_i1</td>
<td>ko:K02978</td>
</tr>
<tr class="even">
<td>1090</td>
<td>TRINITY_DN5679_c0_g1_i1</td>
<td>ko:K17497</td>
</tr>
<tr class="odd">
<td>1121</td>
<td>TRINITY_DN17433_c0_g1_i1</td>
<td>ko:K03358</td>
</tr>
<tr class="even">
<td>1122</td>
<td>TRINITY_DN8861_c0_g1_i1</td>
<td>ko:K02905</td>
</tr>
<tr class="odd">
<td>1124</td>
<td>TRINITY_DN8160_c0_g2_i1</td>
<td>ko:K02872</td>
</tr>
<tr class="even">
<td>1139</td>
<td>TRINITY_DN9233_c0_g1_i1</td>
<td>ko:K02930</td>
</tr>
<tr class="odd">
<td>1141</td>
<td>TRINITY_DN7955_c0_g1_i1</td>
<td>ko:K00856</td>
</tr>
<tr class="even">
<td>1142</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K07901</td>
</tr>
<tr class="odd">
<td>1147</td>
<td>TRINITY_DN9247_c0_g1_i1</td>
<td>ko:K04567</td>
</tr>
<tr class="even">
<td>1151</td>
<td>TRINITY_DN7486_c0_g1_i1</td>
<td>ko:K09499</td>
</tr>
<tr class="odd">
<td>1168</td>
<td>TRINITY_DN5520_c0_g1_i1</td>
<td>ko:K03017</td>
</tr>
<tr class="even">
<td>1185</td>
<td>TRINITY_DN9426_c0_g1_i1</td>
<td>ko:K13448</td>
</tr>
<tr class="odd">
<td>1186</td>
<td>TRINITY_DN8051_c0_g1_i1</td>
<td>ko:K12832</td>
</tr>
<tr class="even">
<td>1191</td>
<td>TRINITY_DN9335_c0_g1_i1</td>
<td>ko:K10949</td>
</tr>
<tr class="odd">
<td>1194</td>
<td>TRINITY_DN9373_c1_g3_i2</td>
<td>ko:K17260</td>
</tr>
<tr class="even">
<td>1195</td>
<td>TRINITY_DN9373_c1_g3_i3</td>
<td>ko:K17260</td>
</tr>
<tr class="odd">
<td>1196</td>
<td>TRINITY_DN9373_c1_g3_i1</td>
<td>ko:K17260</td>
</tr>
<tr class="even">
<td>1197</td>
<td>TRINITY_DN8700_c0_g1_i2</td>
<td>ko:K17080</td>
</tr>
<tr class="odd">
<td>1198</td>
<td>TRINITY_DN8700_c0_g1_i1</td>
<td>ko:K17080</td>
</tr>
<tr class="even">
<td>1201</td>
<td>TRINITY_DN6960_c0_g1_i1</td>
<td>ko:K02739</td>
</tr>
<tr class="odd">
<td>1202</td>
<td>TRINITY_DN25760_c0_g1_i1</td>
<td>ko:K03868</td>
</tr>
<tr class="even">
<td>1209</td>
<td>TRINITY_DN824_c0_g1_i1</td>
<td>ko:K02969</td>
</tr>
<tr class="odd">
<td>1216</td>
<td>TRINITY_DN3336_c0_g1_i1</td>
<td>ko:K10575</td>
</tr>
<tr class="even">
<td>1217</td>
<td>TRINITY_DN3336_c0_g2_i1</td>
<td>ko:K10575</td>
</tr>
<tr class="odd">
<td>1218</td>
<td>TRINITY_DN6793_c0_g1_i1</td>
<td>ko:K10575</td>
</tr>
<tr class="even">
<td>1222</td>
<td>TRINITY_DN9219_c0_g1_i2</td>
<td>ko:K18467</td>
</tr>
<tr class="odd">
<td>1223</td>
<td>TRINITY_DN9219_c0_g1_i1</td>
<td>ko:K18467</td>
</tr>
<tr class="even">
<td>1227</td>
<td>TRINITY_DN8827_c0_g1_i1</td>
<td>ko:K07342</td>
</tr>
<tr class="odd">
<td>1229</td>
<td>TRINITY_DN7127_c0_g1_i1</td>
<td>ko:K02873</td>
</tr>
<tr class="even">
<td>1231</td>
<td>TRINITY_DN5687_c1_g1_i1</td>
<td>ko:K14963</td>
</tr>
<tr class="odd">
<td>1232</td>
<td>TRINITY_DN4830_c0_g1_i1</td>
<td>ko:K12399</td>
</tr>
<tr class="even">
<td>1234</td>
<td>TRINITY_DN1360_c0_g1_i1</td>
<td>ko:K02731</td>
</tr>
<tr class="odd">
<td>1252</td>
<td>TRINITY_DN8231_c0_g1_i2</td>
<td>ko:K07901</td>
</tr>
<tr class="even">
<td>1254</td>
<td>TRINITY_DN8231_c0_g1_i1</td>
<td>ko:K07901</td>
</tr>
<tr class="odd">
<td>1273</td>
<td>TRINITY_DN1426_c0_g1_i1</td>
<td>ko:K10577</td>
</tr>
<tr class="even">
<td>1324</td>
<td>TRINITY_DN8993_c1_g1_i2</td>
<td>ko:K08770</td>
</tr>
<tr class="odd">
<td>1349</td>
<td>TRINITY_DN8355_c0_g1_i1</td>
<td>ko:K05755</td>
</tr>
<tr class="even">
<td>1354</td>
<td>TRINITY_DN9151_c0_g1_i1</td>
<td>ko:K13448</td>
</tr>
<tr class="odd">
<td>1378</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="even">
<td>1379</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="odd">
<td>1380</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07976</td>
</tr>
<tr class="even">
<td>1381</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07877</td>
</tr>
<tr class="odd">
<td>1382</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07877</td>
</tr>
<tr class="even">
<td>1383</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07877</td>
</tr>
<tr class="odd">
<td>1387</td>
<td>TRINITY_DN8731_c0_g2_i1</td>
<td>ko:K07874</td>
</tr>
<tr class="even">
<td>1390</td>
<td>TRINITY_DN8336_c0_g1_i1</td>
<td>ko:K14502</td>
</tr>
<tr class="odd">
<td>1392</td>
<td>TRINITY_DN5049_c0_g1_i1</td>
<td>ko:K06685</td>
</tr>
<tr class="even">
<td>1393</td>
<td>TRINITY_DN5049_c0_g2_i1</td>
<td>ko:K06685</td>
</tr>
<tr class="odd">
<td>1415</td>
<td>TRINITY_DN9132_c0_g1_i1</td>
<td>ko:K01623</td>
</tr>
<tr class="even">
<td>1421</td>
<td>TRINITY_DN9051_c0_g1_i1</td>
<td>ko:K18466</td>
</tr>
<tr class="odd">
<td>1427</td>
<td>TRINITY_DN5194_c0_g1_i1</td>
<td>ko:K11098</td>
</tr>
<tr class="even">
<td>1431</td>
<td>TRINITY_DN9092_c0_g1_i1</td>
<td>ko:K03661</td>
</tr>
<tr class="odd">
<td>1442</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K04392</td>
</tr>
<tr class="even">
<td>1451</td>
<td>TRINITY_DN8969_c0_g1_i1</td>
<td>ko:K01889</td>
</tr>
<tr class="odd">
<td>1452</td>
<td>TRINITY_DN7542_c0_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="even">
<td>1456</td>
<td>TRINITY_DN8637_c0_g1_i1</td>
<td>ko:K02920</td>
</tr>
<tr class="odd">
<td>1479</td>
<td>TRINITY_DN19464_c0_g1_i1</td>
<td>ko:K03038</td>
</tr>
<tr class="even">
<td>1481</td>
<td>TRINITY_DN15336_c0_g1_i1</td>
<td>ko:K12859</td>
</tr>
<tr class="odd">
<td>1484</td>
<td>TRINITY_DN9596_c0_g1_i1</td>
<td>ko:K02133</td>
</tr>
<tr class="even">
<td>1502</td>
<td>TRINITY_DN7353_c0_g1_i1</td>
<td>ko:K03940</td>
</tr>
<tr class="odd">
<td>1503</td>
<td>TRINITY_DN5945_c0_g3_i1</td>
<td>ko:K12833</td>
</tr>
<tr class="even">
<td>1504</td>
<td>TRINITY_DN5945_c0_g2_i1</td>
<td>ko:K12833</td>
</tr>
<tr class="odd">
<td>1505</td>
<td>TRINITY_DN5945_c0_g1_i1</td>
<td>ko:K12833</td>
</tr>
<tr class="even">
<td>1513</td>
<td>TRINITY_DN1681_c0_g1_i1</td>
<td>ko:K02997</td>
</tr>
<tr class="odd">
<td>1544</td>
<td>TRINITY_DN26153_c0_g1_i1</td>
<td>ko:K03030</td>
</tr>
<tr class="even">
<td>1553</td>
<td>TRINITY_DN20720_c0_g1_i1</td>
<td>ko:K12623</td>
</tr>
<tr class="odd">
<td>1577</td>
<td>TRINITY_DN9301_c0_g1_i2</td>
<td>ko:K17080</td>
</tr>
<tr class="even">
<td>1585</td>
<td>TRINITY_DN7401_c0_g1_i1</td>
<td>ko:K03521</td>
</tr>
<tr class="odd">
<td>1604</td>
<td>TRINITY_DN5456_c1_g1_i1</td>
<td>ko:K12624</td>
</tr>
<tr class="even">
<td>1612</td>
<td>TRINITY_DN5335_c0_g1_i1</td>
<td>ko:K12160</td>
</tr>
<tr class="odd">
<td>1644</td>
<td>TRINITY_DN3357_c0_g1_i1</td>
<td>ko:K01802</td>
</tr>
<tr class="even">
<td>1645</td>
<td>TRINITY_DN6945_c1_g1_i1</td>
<td>ko:K01431</td>
</tr>
<tr class="odd">
<td>1654</td>
<td>TRINITY_DN8116_c0_g1_i1</td>
<td>ko:K02705</td>
</tr>
<tr class="even">
<td>1684</td>
<td>TRINITY_DN2467_c0_g1_i1</td>
<td>ko:K02112</td>
</tr>
<tr class="odd">
<td>1685</td>
<td>TRINITY_DN2467_c0_g2_i1</td>
<td>ko:K02112</td>
</tr>
<tr class="even">
<td>1708</td>
<td>TRINITY_DN9310_c0_g1_i1</td>
<td>ko:K04488</td>
</tr>
<tr class="odd">
<td>1724</td>
<td>TRINITY_DN9656_c1_g1_i8</td>
<td>ko:K00819</td>
</tr>
<tr class="even">
<td>1725</td>
<td>TRINITY_DN9656_c1_g1_i9</td>
<td>ko:K00819</td>
</tr>
<tr class="odd">
<td>1726</td>
<td>TRINITY_DN9656_c1_g1_i1</td>
<td>ko:K00819</td>
</tr>
<tr class="even">
<td>1727</td>
<td>TRINITY_DN9656_c1_g1_i2</td>
<td>ko:K00819</td>
</tr>
<tr class="odd">
<td>1728</td>
<td>TRINITY_DN9656_c1_g1_i5</td>
<td>ko:K00819</td>
</tr>
<tr class="even">
<td>1729</td>
<td>TRINITY_DN9656_c1_g1_i7</td>
<td>ko:K00819</td>
</tr>
<tr class="odd">
<td>1730</td>
<td>TRINITY_DN9656_c1_g1_i4</td>
<td>ko:K00819</td>
</tr>
<tr class="even">
<td>1882</td>
<td>TRINITY_DN3986_c0_g1_i1</td>
<td>ko:K10583</td>
</tr>
<tr class="odd">
<td>1883</td>
<td>TRINITY_DN3986_c0_g2_i1</td>
<td>ko:K10583</td>
</tr>
<tr class="even">
<td>1886</td>
<td>TRINITY_DN9427_c0_g1_i1</td>
<td>ko:K01206</td>
</tr>
<tr class="odd">
<td>1887</td>
<td>TRINITY_DN8938_c0_g1_i1</td>
<td>ko:K01206</td>
</tr>
<tr class="even">
<td>1958</td>
<td>TRINITY_DN7111_c0_g1_i1</td>
<td>ko:K03522</td>
</tr>
<tr class="odd">
<td>2015</td>
<td>TRINITY_DN9655_c0_g5_i2</td>
<td>ko:K07374</td>
</tr>
<tr class="even">
<td>2016</td>
<td>TRINITY_DN9616_c0_g2_i6</td>
<td>ko:K07374</td>
</tr>
<tr class="odd">
<td>2017</td>
<td>TRINITY_DN9655_c0_g5_i3</td>
<td>ko:K07374</td>
</tr>
<tr class="even">
<td>2022</td>
<td>TRINITY_DN8751_c0_g1_i1</td>
<td>ko:K08057</td>
</tr>
<tr class="odd">
<td>2044</td>
<td>TRINITY_DN8282_c0_g1_i1</td>
<td>ko:K03232</td>
</tr>
<tr class="even">
<td>2114</td>
<td>TRINITY_DN9618_c0_g1_i2</td>
<td>ko:K03781</td>
</tr>
<tr class="odd">
<td>2147</td>
<td>TRINITY_DN5681_c0_g1_i1</td>
<td>ko:K00616</td>
</tr>
<tr class="even">
<td>2207</td>
<td>TRINITY_DN2882_c0_g1_i1</td>
<td>ko:K16575</td>
</tr>
<tr class="odd">
<td>2210</td>
<td>TRINITY_DN8731_c0_g1_i1</td>
<td>ko:K07901</td>
</tr>
<tr class="even">
<td>2211</td>
<td>TRINITY_DN9501_c0_g2_i1</td>
<td>ko:K18041</td>
</tr>
<tr class="odd">
<td>2212</td>
<td>TRINITY_DN9501_c0_g2_i2</td>
<td>ko:K18041</td>
</tr>
<tr class="even">
<td>2231</td>
<td>TRINITY_DN9214_c0_g1_i1</td>
<td>ko:K01681</td>
</tr>
<tr class="odd">
<td>2232</td>
<td>TRINITY_DN4548_c0_g1_i1</td>
<td>ko:K14394</td>
</tr>
<tr class="even">
<td>2233</td>
<td>TRINITY_DN9299_c0_g1_i1</td>
<td>ko:K18617</td>
</tr>
<tr class="odd">
<td>2234</td>
<td>TRINITY_DN9287_c0_g1_i1</td>
<td>ko:K04456</td>
</tr>
<tr class="even">
<td>2235</td>
<td>TRINITY_DN9287_c0_g1_i2</td>
<td>ko:K04456</td>
</tr>
<tr class="odd">
<td>2237</td>
<td>TRINITY_DN8750_c0_g1_i1</td>
<td>ko:K01363</td>
</tr>
<tr class="even">
<td>2238</td>
<td>TRINITY_DN9355_c0_g1_i2</td>
<td>ko:K01365</td>
</tr>
<tr class="odd">
<td>2239</td>
<td>TRINITY_DN9355_c0_g1_i5</td>
<td>ko:K01365</td>
</tr>
<tr class="even">
<td>2240</td>
<td>TRINITY_DN9355_c0_g1_i4</td>
<td>ko:K01365</td>
</tr>
<tr class="odd">
<td>2241</td>
<td>TRINITY_DN9355_c0_g1_i1</td>
<td>ko:K01365</td>
</tr>
<tr class="even">
<td>2242</td>
<td>TRINITY_DN9653_c1_g1_i1</td>
<td>ko:K01365</td>
</tr>
<tr class="odd">
<td>2243</td>
<td>TRINITY_DN9160_c0_g1_i1</td>
<td>ko:K00207</td>
</tr>
<tr class="even">
<td>2246</td>
<td>TRINITY_DN8161_c0_g1_i1</td>
<td>ko:K00522</td>
</tr>
<tr class="odd">
<td>2251</td>
<td>TRINITY_DN9504_c0_g1_i1</td>
<td>ko:K04536</td>
</tr>
<tr class="even">
<td>2252</td>
<td>TRINITY_DN14077_c0_g1_i1</td>
<td>ko:K00942</td>
</tr>
<tr class="odd">
<td>2254</td>
<td>TRINITY_DN2123_c0_g2_i1</td>
<td>ko:K04551</td>
</tr>
<tr class="even">
<td>2255</td>
<td>TRINITY_DN8993_c1_g1_i4</td>
<td>ko:K04551</td>
</tr>
<tr class="odd">
<td>2257</td>
<td>TRINITY_DN8993_c1_g1_i10</td>
<td>ko:K04551</td>
</tr>
<tr class="even">
<td>2260</td>
<td>TRINITY_DN8528_c0_g1_i1</td>
<td>ko:K09580</td>
</tr>
<tr class="odd">
<td>2261</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K03768</td>
</tr>
<tr class="even">
<td>2263</td>
<td>TRINITY_DN9373_c1_g1_i2</td>
<td>ko:K01074</td>
</tr>
<tr class="odd">
<td>2264</td>
<td>TRINITY_DN9373_c1_g1_i1</td>
<td>ko:K01074</td>
</tr>
<tr class="even">
<td>2267</td>
<td>TRINITY_DN8597_c0_g1_i2</td>
<td>ko:K15103</td>
</tr>
<tr class="odd">
<td>2268</td>
<td>TRINITY_DN8597_c0_g1_i1</td>
<td>ko:K15103</td>
</tr>
<tr class="even">
<td>2269</td>
<td>TRINITY_DN9454_c0_g1_i1</td>
<td>ko:K08007</td>
</tr>
<tr class="odd">
<td>2270</td>
<td>TRINITY_DN9100_c0_g1_i1</td>
<td>ko:K01866</td>
</tr>
<tr class="even">
<td>2273</td>
<td>TRINITY_DN9333_c0_g1_i1</td>
<td>ko:K07249</td>
</tr>
<tr class="odd">
<td>2274</td>
<td>TRINITY_DN6166_c0_g1_i1</td>
<td>ko:K17093</td>
</tr>
<tr class="even">
<td>2275</td>
<td>TRINITY_DN8790_c0_g1_i1</td>
<td>ko:K20472</td>
</tr>
<tr class="odd">
<td>2276</td>
<td>TRINITY_DN14104_c0_g1_i1</td>
<td>ko:K04635</td>
</tr>
<tr class="even">
<td>2277</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04635</td>
</tr>
<tr class="odd">
<td>2278</td>
<td>TRINITY_DN14104_c0_g1_i1</td>
<td>ko:K04636</td>
</tr>
<tr class="even">
<td>2279</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04636</td>
</tr>
<tr class="odd">
<td>2280</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04534</td>
</tr>
<tr class="even">
<td>2281</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04631</td>
</tr>
<tr class="odd">
<td>2283</td>
<td>TRINITY_DN9741_c0_g1_i1</td>
<td>ko:K07509</td>
</tr>
<tr class="even">
<td>2288</td>
<td>TRINITY_DN21425_c0_g1_i1</td>
<td>ko:K04078</td>
</tr>
<tr class="odd">
<td>2290</td>
<td>TRINITY_DN9116_c0_g1_i2</td>
<td>ko:K08548</td>
</tr>
<tr class="even">
<td>2291</td>
<td>TRINITY_DN9116_c0_g1_i1</td>
<td>ko:K08548</td>
</tr>
<tr class="odd">
<td>2293</td>
<td>TRINITY_DN9049_c0_g1_i1</td>
<td>ko:K20011</td>
</tr>
<tr class="even">
<td>2294</td>
<td>TRINITY_DN9049_c0_g1_i1</td>
<td>ko:K03386</td>
</tr>
<tr class="odd">
<td>2295</td>
<td>TRINITY_DN168_c0_g1_i1</td>
<td>ko:K02740</td>
</tr>
<tr class="even">
<td>2296</td>
<td>TRINITY_DN6596_c1_g1_i1</td>
<td>ko:K13280</td>
</tr>
<tr class="odd">
<td>2297</td>
<td>TRINITY_DN8341_c0_g2_i1</td>
<td>ko:K15040</td>
</tr>
<tr class="even">
<td>2298</td>
<td>TRINITY_DN8095_c0_g1_i1</td>
<td>ko:K02146</td>
</tr>
<tr class="odd">
<td>2303</td>
<td>TRINITY_DN6530_c0_g1_i1</td>
<td>ko:K03943</td>
</tr>
<tr class="even">
<td>2306</td>
<td>TRINITY_DN6983_c0_g1_i1</td>
<td>ko:K04345</td>
</tr>
<tr class="odd">
<td>2308</td>
<td>TRINITY_DN8606_c0_g1_i1</td>
<td>ko:K10420</td>
</tr>
<tr class="even">
<td>2309</td>
<td>TRINITY_DN8846_c0_g1_i1</td>
<td>ko:K13785</td>
</tr>
<tr class="odd">
<td>2311</td>
<td>TRINITY_DN6662_c0_g1_i1</td>
<td>ko:K13785</td>
</tr>
<tr class="even">
<td>2312</td>
<td>TRINITY_DN8907_c0_g2_i1</td>
<td>ko:K00414</td>
</tr>
<tr class="odd">
<td>2314</td>
<td>TRINITY_DN9346_c0_g1_i1</td>
<td>ko:K15102</td>
</tr>
<tr class="even">
<td>2338</td>
<td>TRINITY_DN9360_c0_g1_i2</td>
<td>ko:K08957</td>
</tr>
<tr class="odd">
<td>2339</td>
<td>TRINITY_DN7897_c0_g1_i1</td>
<td>ko:K08957</td>
</tr>
<tr class="even">
<td>2340</td>
<td>TRINITY_DN9360_c0_g1_i1</td>
<td>ko:K08957</td>
</tr>
<tr class="odd">
<td>2342</td>
<td>TRINITY_DN8341_c0_g2_i1</td>
<td>ko:K15041</td>
</tr>
<tr class="even">
<td>2349</td>
<td>TRINITY_DN6449_c0_g1_i1</td>
<td>ko:K04348</td>
</tr>
<tr class="odd">
<td>2358</td>
<td>TRINITY_DN8198_c0_g1_i1</td>
<td>ko:K02941</td>
</tr>
<tr class="even">
<td>2359</td>
<td>TRINITY_DN6550_c0_g1_i1</td>
<td>ko:K03942</td>
</tr>
<tr class="odd">
<td>2360</td>
<td>TRINITY_DN8843_c0_g1_i1</td>
<td>ko:K02150</td>
</tr>
<tr class="even">
<td>2361</td>
<td>TRINITY_DN9439_c0_g1_i1</td>
<td>ko:K00411</td>
</tr>
<tr class="odd">
<td>2370</td>
<td>TRINITY_DN15399_c0_g1_i1</td>
<td>ko:K03936</td>
</tr>
<tr class="even">
<td>2374</td>
<td>TRINITY_DN9506_c0_g1_i1</td>
<td>ko:K05757</td>
</tr>
<tr class="odd">
<td>2375</td>
<td>TRINITY_DN7977_c0_g1_i1</td>
<td>ko:K02136</td>
</tr>
<tr class="even">
<td>2377</td>
<td>TRINITY_DN10220_c0_g1_i1</td>
<td>ko:K03950</td>
</tr>
<tr class="odd">
<td>2378</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07860</td>
</tr>
<tr class="even">
<td>2379</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07860</td>
</tr>
<tr class="odd">
<td>2380</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07860</td>
</tr>
<tr class="even">
<td>2381</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07860</td>
</tr>
<tr class="odd">
<td>2382</td>
<td>TRINITY_DN19170_c0_g1_i1</td>
<td>ko:K04371</td>
</tr>
<tr class="even">
<td>2384</td>
<td>TRINITY_DN4436_c0_g1_i1</td>
<td>ko:K12462</td>
</tr>
<tr class="odd">
<td>2385</td>
<td>TRINITY_DN8894_c0_g1_i1</td>
<td>ko:K17292</td>
</tr>
<tr class="even">
<td>2386</td>
<td>TRINITY_DN9116_c0_g1_i2</td>
<td>ko:K08547</td>
</tr>
<tr class="odd">
<td>2387</td>
<td>TRINITY_DN9116_c0_g1_i1</td>
<td>ko:K08547</td>
</tr>
<tr class="even">
<td>2389</td>
<td>TRINITY_DN6041_c0_g1_i1</td>
<td>ko:K02503</td>
</tr>
<tr class="odd">
<td>2390</td>
<td>TRINITY_DN6041_c0_g2_i1</td>
<td>ko:K02503</td>
</tr>
<tr class="even">
<td>2392</td>
<td>TRINITY_DN9653_c1_g1_i1</td>
<td>ko:K01368</td>
</tr>
<tr class="odd">
<td>2393</td>
<td>TRINITY_DN7321_c0_g2_i1</td>
<td>ko:K03949</td>
</tr>
<tr class="even">
<td>2394</td>
<td>TRINITY_DN8651_c0_g1_i1</td>
<td>ko:K02128</td>
</tr>
<tr class="odd">
<td>2402</td>
<td>TRINITY_DN8629_c0_g1_i1</td>
<td>ko:K17268</td>
</tr>
<tr class="even">
<td>2404</td>
<td>TRINITY_DN9625_c1_g1_i2</td>
<td>ko:K08568</td>
</tr>
<tr class="odd">
<td>2405</td>
<td>TRINITY_DN9625_c1_g1_i4</td>
<td>ko:K08568</td>
</tr>
<tr class="even">
<td>2406</td>
<td>TRINITY_DN9625_c1_g1_i3</td>
<td>ko:K08568</td>
</tr>
<tr class="odd">
<td>2407</td>
<td>TRINITY_DN9625_c1_g1_i5</td>
<td>ko:K08568</td>
</tr>
<tr class="even">
<td>2409</td>
<td>TRINITY_DN1064_c0_g1_i1</td>
<td>ko:K08958</td>
</tr>
<tr class="odd">
<td>2410</td>
<td>TRINITY_DN7897_c0_g1_i1</td>
<td>ko:K08958</td>
</tr>
<tr class="even">
<td>2411</td>
<td>TRINITY_DN2209_c0_g1_i1</td>
<td>ko:K14458</td>
</tr>
<tr class="odd">
<td>2412</td>
<td>TRINITY_DN8901_c0_g1_i1</td>
<td>ko:K10435</td>
</tr>
<tr class="even">
<td>2413</td>
<td>TRINITY_DN8446_c0_g1_i2</td>
<td>ko:K10435</td>
</tr>
<tr class="odd">
<td>2414</td>
<td>TRINITY_DN8446_c0_g1_i1</td>
<td>ko:K10435</td>
</tr>
<tr class="even">
<td>2415</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K09565</td>
</tr>
<tr class="odd">
<td>2418</td>
<td>TRINITY_DN24412_c0_g1_i1</td>
<td>ko:K02264</td>
</tr>
<tr class="even">
<td>2420</td>
<td>TRINITY_DN9525_c0_g1_i1</td>
<td>ko:K10056</td>
</tr>
<tr class="odd">
<td>2421</td>
<td>TRINITY_DN9295_c0_g1_i1</td>
<td>ko:K10364</td>
</tr>
<tr class="even">
<td>2422</td>
<td>TRINITY_DN9537_c1_g1_i1</td>
<td>ko:K00544</td>
</tr>
<tr class="odd">
<td>2428</td>
<td>TRINITY_DN9733_c0_g1_i1</td>
<td>ko:K09022</td>
</tr>
<tr class="even">
<td>2442</td>
<td>TRINITY_DN8255_c0_g1_i1</td>
<td>ko:K19682</td>
</tr>
<tr class="odd">
<td>2443</td>
<td>TRINITY_DN8255_c0_g1_i2</td>
<td>ko:K19682</td>
</tr>
<tr class="even">
<td>2445</td>
<td>TRINITY_DN9283_c0_g1_i1</td>
<td>ko:K00249</td>
</tr>
<tr class="odd">
<td>2446</td>
<td>TRINITY_DN9575_c3_g1_i1</td>
<td>ko:K07906</td>
</tr>
<tr class="even">
<td>2448</td>
<td>TRINITY_DN9249_c0_g1_i1</td>
<td>ko:K04712</td>
</tr>
<tr class="odd">
<td>2449</td>
<td>TRINITY_DN3480_c0_g1_i1</td>
<td>ko:K08516</td>
</tr>
<tr class="even">
<td>2450</td>
<td>TRINITY_DN2028_c0_g1_i1</td>
<td>ko:K00927</td>
</tr>
<tr class="odd">
<td>2451</td>
<td>TRINITY_DN9053_c0_g1_i1</td>
<td>ko:K07890</td>
</tr>
<tr class="even">
<td>2454</td>
<td>TRINITY_DN3031_c0_g1_i1</td>
<td>ko:K10436</td>
</tr>
<tr class="odd">
<td>2456</td>
<td>TRINITY_DN251_c0_g1_i1</td>
<td>ko:K05606</td>
</tr>
<tr class="even">
<td>2459</td>
<td>TRINITY_DN6969_c0_g1_i1</td>
<td>ko:K11968</td>
</tr>
<tr class="odd">
<td>2460</td>
<td>TRINITY_DN8473_c0_g1_i1</td>
<td>ko:K00469</td>
</tr>
<tr class="even">
<td>2462</td>
<td>TRINITY_DN2249_c0_g1_i1</td>
<td>ko:K01555</td>
</tr>
<tr class="odd">
<td>2464</td>
<td>TRINITY_DN9167_c0_g1_i1</td>
<td>ko:K08764</td>
</tr>
<tr class="even">
<td>2465</td>
<td>TRINITY_DN4408_c0_g1_i1</td>
<td>ko:K06875</td>
</tr>
<tr class="odd">
<td>2466</td>
<td>TRINITY_DN4408_c0_g2_i1</td>
<td>ko:K06875</td>
</tr>
<tr class="even">
<td>2468</td>
<td>TRINITY_DN9461_c0_g1_i1</td>
<td>ko:K07205</td>
</tr>
<tr class="odd">
<td>2470</td>
<td>TRINITY_DN6152_c0_g1_i1</td>
<td>ko:K19788</td>
</tr>
<tr class="even">
<td>2472</td>
<td>TRINITY_DN6708_c0_g1_i1</td>
<td>ko:K02738</td>
</tr>
<tr class="odd">
<td>2473</td>
<td>TRINITY_DN9576_c0_g1_i1</td>
<td>ko:K22503</td>
</tr>
<tr class="even">
<td>2474</td>
<td>TRINITY_DN9400_c0_g1_i1</td>
<td>ko:K00967</td>
</tr>
<tr class="odd">
<td>2477</td>
<td>TRINITY_DN7120_c0_g1_i1</td>
<td>ko:K00500</td>
</tr>
<tr class="even">
<td>2478</td>
<td>TRINITY_DN6708_c0_g1_i1</td>
<td>ko:K02741</td>
</tr>
<tr class="odd">
<td>2479</td>
<td>TRINITY_DN9621_c0_g1_i1</td>
<td>ko:K12670</td>
</tr>
<tr class="even">
<td>2481</td>
<td>TRINITY_DN7780_c0_g1_i1</td>
<td>ko:K01892</td>
</tr>
<tr class="odd">
<td>2483</td>
<td>TRINITY_DN9430_c0_g1_i2</td>
<td>ko:K07955</td>
</tr>
<tr class="even">
<td>2485</td>
<td>TRINITY_DN2394_c0_g1_i1</td>
<td>ko:K05687</td>
</tr>
<tr class="odd">
<td>2486</td>
<td>TRINITY_DN12735_c0_g1_i1</td>
<td>ko:K15455</td>
</tr>
<tr class="even">
<td>2487</td>
<td>TRINITY_DN7851_c0_g1_i1</td>
<td>ko:K12197</td>
</tr>
<tr class="odd">
<td>2488</td>
<td>TRINITY_DN8810_c0_g1_i1</td>
<td>ko:K12197</td>
</tr>
<tr class="even">
<td>2490</td>
<td>TRINITY_DN6884_c0_g1_i1</td>
<td>ko:K00413</td>
</tr>
<tr class="odd">
<td>2491</td>
<td>TRINITY_DN10805_c0_g1_i1</td>
<td>ko:K19400</td>
</tr>
<tr class="even">
<td>2493</td>
<td>TRINITY_DN14587_c0_g1_i1</td>
<td>ko:K03104</td>
</tr>
<tr class="odd">
<td>2494</td>
<td>TRINITY_DN7344_c0_g1_i1</td>
<td>ko:K03031</td>
</tr>
<tr class="even">
<td>2495</td>
<td>TRINITY_DN9653_c1_g1_i1</td>
<td>ko:K01371</td>
</tr>
<tr class="odd">
<td>2497</td>
<td>TRINITY_DN674_c0_g1_i1</td>
<td>ko:K12602</td>
</tr>
<tr class="even">
<td>2498</td>
<td>TRINITY_DN8390_c0_g1_i1</td>
<td>ko:K03626</td>
</tr>
<tr class="odd">
<td>2502</td>
<td>TRINITY_DN5468_c0_g1_i1</td>
<td>ko:K00966</td>
</tr>
<tr class="even">
<td>2503</td>
<td>TRINITY_DN5468_c0_g2_i1</td>
<td>ko:K00966</td>
</tr>
<tr class="odd">
<td>2504</td>
<td>TRINITY_DN9223_c0_g1_i1</td>
<td>ko:K01953</td>
</tr>
<tr class="even">
<td>2505</td>
<td>TRINITY_DN7419_c0_g1_i1</td>
<td>ko:K02732</td>
</tr>
<tr class="odd">
<td>2507</td>
<td>TRINITY_DN9347_c0_g1_i1</td>
<td>ko:K17920</td>
</tr>
<tr class="even">
<td>2508</td>
<td>TRINITY_DN8927_c0_g1_i2</td>
<td>ko:K00456</td>
</tr>
<tr class="odd">
<td>2509</td>
<td>TRINITY_DN8927_c0_g1_i1</td>
<td>ko:K00456</td>
</tr>
<tr class="even">
<td>2510</td>
<td>TRINITY_DN8731_c0_g1_i1</td>
<td>ko:K06109</td>
</tr>
<tr class="odd">
<td>2511</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K06109</td>
</tr>
<tr class="even">
<td>2516</td>
<td>TRINITY_DN2922_c0_g2_i1</td>
<td>ko:K12398</td>
</tr>
<tr class="odd">
<td>2518</td>
<td>TRINITY_DN20707_c0_g1_i1</td>
<td>ko:K09570</td>
</tr>
<tr class="even">
<td>2521</td>
<td>TRINITY_DN9437_c0_g2_i2</td>
<td>ko:K14286</td>
</tr>
<tr class="odd">
<td>2525</td>
<td>TRINITY_DN11838_c0_g1_i1</td>
<td>ko:K15028</td>
</tr>
<tr class="even">
<td>2526</td>
<td>TRINITY_DN9301_c0_g1_i1</td>
<td>ko:K17081</td>
</tr>
<tr class="odd">
<td>2529</td>
<td>TRINITY_DN6523_c0_g1_i1</td>
<td>ko:K02725</td>
</tr>
<tr class="even">
<td>2532</td>
<td>TRINITY_DN8936_c0_g1_i1</td>
<td>ko:K12393</td>
</tr>
<tr class="odd">
<td>2534</td>
<td>TRINITY_DN8422_c0_g1_i2</td>
<td>ko:K04500</td>
</tr>
<tr class="even">
<td>2535</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K19729</td>
</tr>
<tr class="odd">
<td>2536</td>
<td>TRINITY_DN7886_c0_g1_i1</td>
<td>ko:K17266</td>
</tr>
<tr class="even">
<td>2537</td>
<td>TRINITY_DN7341_c0_g1_i1</td>
<td>ko:K02734</td>
</tr>
<tr class="odd">
<td>2544</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="even">
<td>2545</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="odd">
<td>2546</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="even">
<td>2547</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07939</td>
</tr>
<tr class="odd">
<td>2548</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="even">
<td>2549</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="odd">
<td>2554</td>
<td>TRINITY_DN8964_c0_g1_i1</td>
<td>ko:K08872</td>
</tr>
<tr class="even">
<td>2555</td>
<td>TRINITY_DN14422_c0_g1_i1</td>
<td>ko:K09658</td>
</tr>
<tr class="odd">
<td>2557</td>
<td>TRINITY_DN7471_c0_g1_i1</td>
<td>ko:K04503</td>
</tr>
<tr class="even">
<td>2558</td>
<td>TRINITY_DN19360_c0_g1_i1</td>
<td>ko:K07952</td>
</tr>
<tr class="odd">
<td>2559</td>
<td>TRINITY_DN9530_c0_g1_i1</td>
<td>ko:K20369</td>
</tr>
<tr class="even">
<td>2564</td>
<td>TRINITY_DN9157_c0_g1_i1</td>
<td>ko:K20352</td>
</tr>
<tr class="odd">
<td>2565</td>
<td>TRINITY_DN9157_c0_g1_i2</td>
<td>ko:K20352</td>
</tr>
<tr class="even">
<td>2568</td>
<td>TRINITY_DN9114_c0_g1_i3</td>
<td>ko:K12757</td>
</tr>
<tr class="odd">
<td>2569</td>
<td>TRINITY_DN6480_c0_g1_i1</td>
<td>ko:K12757</td>
</tr>
<tr class="even">
<td>2570</td>
<td>TRINITY_DN9024_c0_g1_i1</td>
<td>ko:K12757</td>
</tr>
<tr class="odd">
<td>2571</td>
<td>TRINITY_DN9114_c0_g1_i2</td>
<td>ko:K12757</td>
</tr>
<tr class="even">
<td>2572</td>
<td>TRINITY_DN9114_c0_g1_i1</td>
<td>ko:K12757</td>
</tr>
<tr class="odd">
<td>2574</td>
<td>TRINITY_DN9495_c0_g1_i2</td>
<td>ko:K10705</td>
</tr>
<tr class="even">
<td>2575</td>
<td>TRINITY_DN9495_c0_g1_i1</td>
<td>ko:K10705</td>
</tr>
<tr class="odd">
<td>2576</td>
<td>TRINITY_DN6629_c0_g2_i1</td>
<td>ko:K15620</td>
</tr>
<tr class="even">
<td>2577</td>
<td>TRINITY_DN6629_c0_g1_i1</td>
<td>ko:K15620</td>
</tr>
<tr class="odd">
<td>2578</td>
<td>TRINITY_DN9397_c0_g1_i1</td>
<td>ko:K07192</td>
</tr>
<tr class="even">
<td>2579</td>
<td>TRINITY_DN9397_c0_g1_i2</td>
<td>ko:K07192</td>
</tr>
<tr class="odd">
<td>2584</td>
<td>TRINITY_DN4140_c0_g1_i1</td>
<td>ko:K15153</td>
</tr>
<tr class="even">
<td>2585</td>
<td>TRINITY_DN7498_c0_g1_i1</td>
<td>ko:K04370</td>
</tr>
<tr class="odd">
<td>2588</td>
<td>TRINITY_DN8907_c0_g2_i1</td>
<td>ko:K17732</td>
</tr>
<tr class="even">
<td>2589</td>
<td>TRINITY_DN168_c0_g1_i1</td>
<td>ko:K02737</td>
</tr>
<tr class="odd">
<td>2598</td>
<td>TRINITY_DN9783_c0_g1_i1</td>
<td>ko:K12620</td>
</tr>
<tr class="even">
<td>2599</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K09563</td>
</tr>
<tr class="odd">
<td>2607</td>
<td>TRINITY_DN10058_c0_g1_i1</td>
<td>ko:K11659</td>
</tr>
<tr class="even">
<td>2608</td>
<td>TRINITY_DN16198_c0_g1_i1</td>
<td>ko:K10411</td>
</tr>
<tr class="odd">
<td>2610</td>
<td>TRINITY_DN6990_c0_g1_i1</td>
<td>ko:K09569</td>
</tr>
<tr class="even">
<td>2612</td>
<td>TRINITY_DN9608_c0_g1_i2</td>
<td>ko:K01758</td>
</tr>
<tr class="odd">
<td>2613</td>
<td>TRINITY_DN9608_c0_g1_i1</td>
<td>ko:K01758</td>
</tr>
<tr class="even">
<td>2614</td>
<td>TRINITY_DN8382_c0_g1_i1</td>
<td>ko:K00814</td>
</tr>
<tr class="odd">
<td>2615</td>
<td>TRINITY_DN5674_c0_g1_i1</td>
<td>ko:K01527</td>
</tr>
<tr class="even">
<td>2616</td>
<td>TRINITY_DN8941_c0_g1_i1</td>
<td>ko:K07887</td>
</tr>
<tr class="odd">
<td>2625</td>
<td>TRINITY_DN9454_c0_g1_i1</td>
<td>ko:K05763</td>
</tr>
<tr class="even">
<td>2626</td>
<td>TRINITY_DN8422_c0_g1_i2</td>
<td>ko:K04676</td>
</tr>
<tr class="odd">
<td>2627</td>
<td>TRINITY_DN7471_c0_g1_i1</td>
<td>ko:K10152</td>
</tr>
<tr class="even">
<td>2628</td>
<td>TRINITY_DN8231_c0_g1_i1</td>
<td>ko:K07875</td>
</tr>
<tr class="odd">
<td>2629</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K07875</td>
</tr>
<tr class="even">
<td>2630</td>
<td>TRINITY_DN8231_c0_g1_i2</td>
<td>ko:K07875</td>
</tr>
<tr class="odd">
<td>2631</td>
<td>TRINITY_DN8731_c0_g2_i1</td>
<td>ko:K07875</td>
</tr>
<tr class="even">
<td>2632</td>
<td>TRINITY_DN7538_c0_g1_i1</td>
<td>ko:K17795</td>
</tr>
<tr class="odd">
<td>2640</td>
<td>TRINITY_DN6815_c0_g1_i1</td>
<td>ko:K20791</td>
</tr>
<tr class="even">
<td>2641</td>
<td>TRINITY_DN8618_c0_g1_i1</td>
<td>ko:K12194</td>
</tr>
<tr class="odd">
<td>2642</td>
<td>TRINITY_DN8941_c0_g1_i1</td>
<td>ko:K07889</td>
</tr>
<tr class="even">
<td>2643</td>
<td>TRINITY_DN1242_c0_g1_i1</td>
<td>ko:K08515</td>
</tr>
<tr class="odd">
<td>2649</td>
<td>TRINITY_DN3541_c0_g1_i1</td>
<td>ko:K17771</td>
</tr>
<tr class="even">
<td>2651</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K07902</td>
</tr>
<tr class="odd">
<td>2652</td>
<td>TRINITY_DN8731_c0_g1_i1</td>
<td>ko:K07902</td>
</tr>
<tr class="even">
<td>2653</td>
<td>TRINITY_DN9414_c0_g1_i2</td>
<td>ko:K05754</td>
</tr>
<tr class="odd">
<td>2654</td>
<td>TRINITY_DN9414_c0_g1_i1</td>
<td>ko:K05754</td>
</tr>
<tr class="even">
<td>2655</td>
<td>TRINITY_DN3336_c0_g2_i1</td>
<td>ko:K04555</td>
</tr>
<tr class="odd">
<td>2656</td>
<td>TRINITY_DN3336_c0_g1_i1</td>
<td>ko:K04555</td>
</tr>
<tr class="even">
<td>2660</td>
<td>TRINITY_DN6020_c0_g2_i1</td>
<td>ko:K15544</td>
</tr>
<tr class="odd">
<td>2661</td>
<td>TRINITY_DN8653_c0_g1_i1</td>
<td>ko:K02891</td>
</tr>
<tr class="even">
<td>2666</td>
<td>TRINITY_DN3374_c0_g2_i1</td>
<td>ko:K12669</td>
</tr>
<tr class="odd">
<td>2667</td>
<td>TRINITY_DN3374_c0_g1_i1</td>
<td>ko:K12669</td>
</tr>
<tr class="even">
<td>2672</td>
<td>TRINITY_DN7006_c0_g1_i1</td>
<td>ko:K04739</td>
</tr>
<tr class="odd">
<td>2686</td>
<td>TRINITY_DN8549_c0_g1_i1</td>
<td>ko:K04444</td>
</tr>
<tr class="even">
<td>2687</td>
<td>TRINITY_DN7471_c0_g1_i1</td>
<td>ko:K10151</td>
</tr>
<tr class="odd">
<td>2691</td>
<td>TRINITY_DN1731_c0_g1_i1</td>
<td>ko:K14324</td>
</tr>
<tr class="even">
<td>2692</td>
<td>TRINITY_DN6997_c0_g1_i1</td>
<td>ko:K15025</td>
</tr>
<tr class="odd">
<td>2694</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07879</td>
</tr>
<tr class="even">
<td>2695</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07879</td>
</tr>
<tr class="odd">
<td>2696</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07879</td>
</tr>
<tr class="even">
<td>2697</td>
<td>TRINITY_DN9570_c0_g1_i1</td>
<td>ko:K01893</td>
</tr>
<tr class="odd">
<td>2698</td>
<td>TRINITY_DN26366_c0_g1_i1</td>
<td>ko:K00419</td>
</tr>
<tr class="even">
<td>2700</td>
<td>TRINITY_DN9182_c0_g1_i1</td>
<td>ko:K19931</td>
</tr>
<tr class="odd">
<td>2701</td>
<td>TRINITY_DN9182_c0_g1_i2</td>
<td>ko:K19931</td>
</tr>
<tr class="even">
<td>2706</td>
<td>TRINITY_DN7128_c0_g1_i1</td>
<td>ko:K20301</td>
</tr>
<tr class="odd">
<td>2716</td>
<td>TRINITY_DN7173_c0_g1_i1</td>
<td>ko:K10704</td>
</tr>
<tr class="even">
<td>2717</td>
<td>TRINITY_DN7173_c0_g1_i2</td>
<td>ko:K10704</td>
</tr>
<tr class="odd">
<td>2718</td>
<td>TRINITY_DN3286_c0_g1_i1</td>
<td>ko:K00357</td>
</tr>
<tr class="even">
<td>2719</td>
<td>TRINITY_DN7414_c0_g1_i1</td>
<td>ko:K17780</td>
</tr>
<tr class="odd">
<td>2722</td>
<td>TRINITY_DN7461_c0_g1_i1</td>
<td>ko:K20346</td>
</tr>
<tr class="even">
<td>2723</td>
<td>TRINITY_DN7461_c0_g2_i1</td>
<td>ko:K20346</td>
</tr>
<tr class="odd">
<td>2728</td>
<td>TRINITY_DN7870_c0_g1_i1</td>
<td>ko:K19765</td>
</tr>
<tr class="even">
<td>2729</td>
<td>TRINITY_DN7508_c0_g1_i1</td>
<td>ko:K13251</td>
</tr>
<tr class="odd">
<td>2735</td>
<td>TRINITY_DN5319_c0_g1_i1</td>
<td>ko:K10419</td>
</tr>
<tr class="even">
<td>2736</td>
<td>TRINITY_DN5319_c0_g2_i1</td>
<td>ko:K10419</td>
</tr>
<tr class="odd">
<td>2738</td>
<td>TRINITY_DN6056_c0_g1_i1</td>
<td>ko:K08762</td>
</tr>
<tr class="even">
<td>2755</td>
<td>TRINITY_DN8436_c1_g2_i1</td>
<td>ko:K11279</td>
</tr>
<tr class="odd">
<td>2875</td>
<td>TRINITY_DN8872_c0_g2_i1</td>
<td>ko:K15427</td>
</tr>
<tr class="even">
<td>2923</td>
<td>TRINITY_DN14631_c0_g1_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="odd">
<td>2924</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="even">
<td>2925</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="odd">
<td>2926</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07977</td>
</tr>
<tr class="even">
<td>2999</td>
<td>TRINITY_DN14400_c0_g1_i1</td>
<td>ko:K07937</td>
</tr>
<tr class="odd">
<td>3007</td>
<td>TRINITY_DN5998_c0_g1_i1</td>
<td>ko:K02149</td>
</tr>
<tr class="even">
<td>3056</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07827</td>
</tr>
<tr class="odd">
<td>3058</td>
<td>TRINITY_DN6662_c0_g1_i1</td>
<td>ko:K05764</td>
</tr>
<tr class="even">
<td>3062</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K10354</td>
</tr>
<tr class="odd">
<td>3142</td>
<td>TRINITY_DN8974_c0_g1_i3</td>
<td>ko:K09584</td>
</tr>
<tr class="even">
<td>3143</td>
<td>TRINITY_DN8974_c0_g1_i2</td>
<td>ko:K09584</td>
</tr>
<tr class="odd">
<td>3144</td>
<td>TRINITY_DN8974_c0_g1_i1</td>
<td>ko:K09584</td>
</tr>
<tr class="even">
<td>3153</td>
<td>TRINITY_DN6537_c0_g1_i1</td>
<td>ko:K12873</td>
</tr>
<tr class="odd">
<td>3154</td>
<td>TRINITY_DN6537_c0_g2_i1</td>
<td>ko:K12873</td>
</tr>
<tr class="even">
<td>3157</td>
<td>TRINITY_DN10866_c0_g1_i1</td>
<td>ko:K04392</td>
</tr>
<tr class="odd">
<td>3159</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K04392</td>
</tr>
<tr class="even">
<td>3164</td>
<td>TRINITY_DN7443_c0_g1_i1</td>
<td>ko:K02889</td>
</tr>
<tr class="odd">
<td>3165</td>
<td>TRINITY_DN512_c0_g1_i1</td>
<td>ko:K04364</td>
</tr>
<tr class="even">
<td>3185</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K04353</td>
</tr>
<tr class="odd">
<td>3186</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K04353</td>
</tr>
<tr class="even">
<td>3221</td>
<td>TRINITY_DN5413_c0_g1_i1</td>
<td>ko:K19932</td>
</tr>
<tr class="odd">
<td>3233</td>
<td>TRINITY_DN6037_c0_g2_i1</td>
<td>ko:K11096</td>
</tr>
<tr class="even">
<td>3251</td>
<td>TRINITY_DN9152_c0_g1_i1</td>
<td>ko:K02882</td>
</tr>
<tr class="odd">
<td>3291</td>
<td>TRINITY_DN9391_c0_g1_i1</td>
<td>ko:K01890</td>
</tr>
<tr class="even">
<td>3350</td>
<td>TRINITY_DN17244_c0_g1_i1</td>
<td>ko:K12158</td>
</tr>
<tr class="odd">
<td>3377</td>
<td>TRINITY_DN7101_c0_g1_i1</td>
<td>ko:K02951</td>
</tr>
<tr class="even">
<td>3443</td>
<td>TRINITY_DN8626_c0_g1_i1</td>
<td>ko:K08794</td>
</tr>
<tr class="odd">
<td>3462</td>
<td>TRINITY_DN9093_c0_g1_i1</td>
<td>ko:K06630</td>
</tr>
<tr class="even">
<td>3472</td>
<td>TRINITY_DN17839_c0_g1_i1</td>
<td>ko:K06689</td>
</tr>
<tr class="odd">
<td>3489</td>
<td>TRINITY_DN8745_c0_g2_i1</td>
<td>ko:K03115</td>
</tr>
<tr class="even">
<td>3490</td>
<td>TRINITY_DN8745_c0_g2_i2</td>
<td>ko:K03115</td>
</tr>
<tr class="odd">
<td>3527</td>
<td>TRINITY_DN24681_c0_g1_i1</td>
<td>ko:K14803</td>
</tr>
<tr class="even">
<td>3535</td>
<td>TRINITY_DN7547_c0_g1_i1</td>
<td>ko:K11087</td>
</tr>
<tr class="odd">
<td>3537</td>
<td>TRINITY_DN8500_c0_g1_i1</td>
<td>ko:K20347</td>
</tr>
<tr class="even">
<td>3544</td>
<td>TRINITY_DN7251_c0_g1_i2</td>
<td>ko:K11088</td>
</tr>
<tr class="odd">
<td>3545</td>
<td>TRINITY_DN7251_c0_g1_i1</td>
<td>ko:K11088</td>
</tr>
<tr class="even">
<td>3548</td>
<td>TRINITY_DN19131_c0_g1_i1</td>
<td>ko:K04077</td>
</tr>
<tr class="odd">
<td>3550</td>
<td>TRINITY_DN19239_c0_g1_i1</td>
<td>ko:K05756</td>
</tr>
<tr class="even">
<td>3561</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K03767</td>
</tr>
<tr class="odd">
<td>3562</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K03767</td>
</tr>
<tr class="even">
<td>3626</td>
<td>TRINITY_DN6618_c0_g1_i1</td>
<td>ko:K03109</td>
</tr>
<tr class="odd">
<td>3642</td>
<td>TRINITY_DN9355_c0_g1_i5</td>
<td>ko:K01368</td>
</tr>
<tr class="even">
<td>3643</td>
<td>TRINITY_DN9355_c0_g1_i2</td>
<td>ko:K01368</td>
</tr>
<tr class="odd">
<td>3644</td>
<td>TRINITY_DN9355_c0_g1_i4</td>
<td>ko:K01368</td>
</tr>
<tr class="even">
<td>3648</td>
<td>TRINITY_DN9504_c0_g1_i1</td>
<td>ko:K07825</td>
</tr>
<tr class="odd">
<td>3658</td>
<td>TRINITY_DN6518_c0_g1_i1</td>
<td>ko:K07213</td>
</tr>
<tr class="even">
<td>3665</td>
<td>TRINITY_DN14104_c0_g1_i1</td>
<td>ko:K04634</td>
</tr>
<tr class="odd">
<td>3666</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04634</td>
</tr>
<tr class="even">
<td>3669</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07880</td>
</tr>
<tr class="odd">
<td>3670</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07880</td>
</tr>
<tr class="even">
<td>3673</td>
<td>TRINITY_DN6752_c0_g1_i1</td>
<td>ko:K12948</td>
</tr>
<tr class="odd">
<td>3679</td>
<td>TRINITY_DN8713_c0_g1_i1</td>
<td>ko:K09481</td>
</tr>
<tr class="even">
<td>3697</td>
<td>TRINITY_DN7370_c0_g1_i1</td>
<td>ko:K04369</td>
</tr>
<tr class="odd">
<td>3723</td>
<td>TRINITY_DN8298_c0_g1_i1</td>
<td>ko:K01875</td>
</tr>
<tr class="even">
<td>3726</td>
<td>TRINITY_DN9049_c0_g1_i1</td>
<td>ko:K13279</td>
</tr>
<tr class="odd">
<td>3731</td>
<td>TRINITY_DN7370_c0_g1_i1</td>
<td>ko:K04368</td>
</tr>
<tr class="even">
<td>3744</td>
<td>TRINITY_DN20068_c0_g1_i1</td>
<td>ko:K03014</td>
</tr>
<tr class="odd">
<td>3932</td>
<td>TRINITY_DN7177_c0_g1_i1</td>
<td>ko:K05361</td>
</tr>
<tr class="even">
<td>3987</td>
<td>TRINITY_DN5817_c0_g1_i1</td>
<td>ko:K02994</td>
</tr>
<tr class="odd">
<td>4038</td>
<td>TRINITY_DN8050_c0_g1_i1</td>
<td>ko:K09569</td>
</tr>
<tr class="even">
<td>4039</td>
<td>TRINITY_DN7979_c0_g1_i1</td>
<td>ko:K17918</td>
</tr>
<tr class="odd">
<td>4165</td>
<td>TRINITY_DN13571_c0_g1_i1</td>
<td>ko:K02929</td>
</tr>
<tr class="even">
<td>4395</td>
<td>TRINITY_DN9027_c0_g1_i1</td>
<td>ko:K22556</td>
</tr>
<tr class="odd">
<td>4428</td>
<td>TRINITY_DN9402_c0_g1_i1</td>
<td>ko:K01697</td>
</tr>
<tr class="even">
<td>4429</td>
<td>TRINITY_DN9402_c0_g1_i2</td>
<td>ko:K01697</td>
</tr>
<tr class="odd">
<td>4447</td>
<td>TRINITY_DN9513_c2_g4_i1</td>
<td>ko:K10355</td>
</tr>
<tr class="even">
<td>4481</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07975</td>
</tr>
<tr class="odd">
<td>4482</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07975</td>
</tr>
<tr class="even">
<td>4524</td>
<td>TRINITY_DN7897_c0_g1_i1</td>
<td>ko:K14758</td>
</tr>
<tr class="odd">
<td>4536</td>
<td>TRINITY_DN8231_c0_g1_i2</td>
<td>ko:K07976</td>
</tr>
<tr class="even">
<td>4537</td>
<td>TRINITY_DN8231_c0_g1_i1</td>
<td>ko:K07976</td>
</tr>
<tr class="odd">
<td>4588</td>
<td>TRINITY_DN9575_c3_g1_i1</td>
<td>ko:K07905</td>
</tr>
<tr class="even">
<td>4590</td>
<td>TRINITY_DN7458_c0_g1_i1</td>
<td>ko:K20302</td>
</tr>
<tr class="odd">
<td>4607</td>
<td>TRINITY_DN9142_c0_g1_i1</td>
<td>ko:K03236</td>
</tr>
<tr class="even">
<td>4661</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07881</td>
</tr>
<tr class="odd">
<td>4662</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07881</td>
</tr>
<tr class="even">
<td>4663</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07881</td>
</tr>
<tr class="odd">
<td>4679</td>
<td>TRINITY_DN8872_c0_g2_i1</td>
<td>ko:K17615</td>
</tr>
<tr class="even">
<td>4681</td>
<td>TRINITY_DN8558_c0_g1_i1</td>
<td>ko:K07918</td>
</tr>
<tr class="odd">
<td>4703</td>
<td>TRINITY_DN25838_c0_g1_i1</td>
<td>ko:K10753</td>
</tr>
<tr class="even">
<td>4724</td>
<td>TRINITY_DN8347_c0_g1_i1</td>
<td>ko:K02915</td>
</tr>
<tr class="odd">
<td>4758</td>
<td>TRINITY_DN10348_c0_g1_i1</td>
<td>ko:K16185</td>
</tr>
<tr class="even">
<td>4783</td>
<td>TRINITY_DN2209_c0_g1_i1</td>
<td>ko:K14457</td>
</tr>
<tr class="odd">
<td>4796</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07836</td>
</tr>
<tr class="even">
<td>4813</td>
<td>TRINITY_DN8814_c0_g1_i2</td>
<td>ko:K12191</td>
</tr>
<tr class="odd">
<td>4814</td>
<td>TRINITY_DN8814_c0_g1_i1</td>
<td>ko:K12191</td>
</tr>
<tr class="even">
<td>4825</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07975</td>
</tr>
<tr class="odd">
<td>4826</td>
<td>TRINITY_DN9515_c0_g1_i1</td>
<td>ko:K13126</td>
</tr>
<tr class="even">
<td>4835</td>
<td>TRINITY_DN2492_c0_g1_i1</td>
<td>ko:K12826</td>
</tr>
<tr class="odd">
<td>4902</td>
<td>TRINITY_DN8301_c0_g1_i1</td>
<td>ko:K10574</td>
</tr>
<tr class="even">
<td>4988</td>
<td>TRINITY_DN9025_c0_g2_i1</td>
<td>ko:K01090</td>
</tr>
<tr class="odd">
<td>5003</td>
<td>TRINITY_DN6959_c0_g1_i1</td>
<td>ko:K06268</td>
</tr>
<tr class="even">
<td>5010</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K07830</td>
</tr>
<tr class="odd">
<td>5011</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K07830</td>
</tr>
<tr class="even">
<td>5032</td>
<td>TRINITY_DN8278_c0_g1_i1</td>
<td>ko:K04552</td>
</tr>
<tr class="odd">
<td>5046</td>
<td>TRINITY_DN5313_c0_g1_i1</td>
<td>ko:K02947</td>
</tr>
<tr class="even">
<td>5103</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K04353</td>
</tr>
<tr class="odd">
<td>5109</td>
<td>TRINITY_DN7897_c0_g1_i1</td>
<td>ko:K08960</td>
</tr>
<tr class="even">
<td>5147</td>
<td>TRINITY_DN8549_c0_g1_i1</td>
<td>ko:K04443</td>
</tr>
<tr class="odd">
<td>5170</td>
<td>TRINITY_DN6276_c0_g1_i1</td>
<td>ko:K12751</td>
</tr>
<tr class="even">
<td>5399</td>
<td>TRINITY_DN20351_c0_g1_i1</td>
<td>ko:K18211</td>
</tr>
<tr class="odd">
<td>5404</td>
<td>TRINITY_DN20637_c0_g1_i1</td>
<td>ko:K22071</td>
</tr>
<tr class="even">
<td>5410</td>
<td>TRINITY_DN4855_c0_g1_i1</td>
<td>ko:K03012</td>
</tr>
<tr class="odd">
<td>5419</td>
<td>TRINITY_DN6159_c0_g1_i1</td>
<td>ko:K03123</td>
</tr>
<tr class="even">
<td>5420</td>
<td>TRINITY_DN6159_c0_g2_i1</td>
<td>ko:K03123</td>
</tr>
<tr class="odd">
<td>5423</td>
<td>TRINITY_DN8585_c0_g1_i1</td>
<td>ko:K20398</td>
</tr>
<tr class="even">
<td>5451</td>
<td>TRINITY_DN8360_c0_g1_i1</td>
<td>ko:K04364</td>
</tr>
<tr class="odd">
<td>5457</td>
<td>TRINITY_DN3619_c0_g1_i1</td>
<td>ko:K02152</td>
</tr>
<tr class="even">
<td>5458</td>
<td>TRINITY_DN8821_c0_g1_i1</td>
<td>ko:K04354</td>
</tr>
<tr class="odd">
<td>5459</td>
<td>TRINITY_DN7922_c0_g1_i1</td>
<td>ko:K12198</td>
</tr>
<tr class="even">
<td>5468</td>
<td>TRINITY_DN7459_c0_g1_i1</td>
<td>ko:K02975</td>
</tr>
<tr class="odd">
<td>5470</td>
<td>TRINITY_DN6341_c0_g1_i1</td>
<td>ko:K20217</td>
</tr>
<tr class="even">
<td>5488</td>
<td>TRINITY_DN7090_c0_g1_i1</td>
<td>ko:K21870</td>
</tr>
<tr class="odd">
<td>5510</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07941</td>
</tr>
<tr class="even">
<td>5511</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07941</td>
</tr>
<tr class="odd">
<td>5512</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07941</td>
</tr>
<tr class="even">
<td>5513</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07941</td>
</tr>
<tr class="odd">
<td>5600</td>
<td>TRINITY_DN4250_c0_g1_i1</td>
<td>ko:K03237</td>
</tr>
<tr class="even">
<td>5691</td>
<td>TRINITY_DN9134_c0_g2_i1</td>
<td>ko:K16198</td>
</tr>
<tr class="odd">
<td>5692</td>
<td>TRINITY_DN9093_c0_g1_i1</td>
<td>ko:K16198</td>
</tr>
<tr class="even">
<td>5693</td>
<td>TRINITY_DN7767_c0_g1_i1</td>
<td>ko:K16198</td>
</tr>
<tr class="odd">
<td>5694</td>
<td>TRINITY_DN8511_c0_g1_i1</td>
<td>ko:K16198</td>
</tr>
<tr class="even">
<td>5695</td>
<td>TRINITY_DN9134_c0_g1_i2</td>
<td>ko:K16198</td>
</tr>
<tr class="odd">
<td>5696</td>
<td>TRINITY_DN9134_c0_g1_i3</td>
<td>ko:K16198</td>
</tr>
<tr class="even">
<td>5697</td>
<td>TRINITY_DN9134_c0_g2_i2</td>
<td>ko:K16198</td>
</tr>
<tr class="odd">
<td>5704</td>
<td>TRINITY_DN7748_c0_g1_i1</td>
<td>ko:K02896</td>
</tr>
<tr class="even">
<td>5714</td>
<td>TRINITY_DN9116_c0_g1_i1</td>
<td>ko:K08702</td>
</tr>
<tr class="odd">
<td>5715</td>
<td>TRINITY_DN9116_c0_g1_i2</td>
<td>ko:K08702</td>
</tr>
<tr class="even">
<td>5721</td>
<td>TRINITY_DN9547_c0_g1_i1</td>
<td>ko:K04079</td>
</tr>
<tr class="odd">
<td>5731</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K07836</td>
</tr>
<tr class="even">
<td>5732</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K07836</td>
</tr>
<tr class="odd">
<td>5738</td>
<td>TRINITY_DN7897_c0_g1_i1</td>
<td>ko:K08959</td>
</tr>
<tr class="even">
<td>5753</td>
<td>TRINITY_DN26_c0_g2_i1</td>
<td>ko:K03015</td>
</tr>
<tr class="odd">
<td>5754</td>
<td>TRINITY_DN26_c0_g1_i1</td>
<td>ko:K03015</td>
</tr>
<tr class="even">
<td>5755</td>
<td>TRINITY_DN3374_c0_g1_i1</td>
<td>ko:K19478</td>
</tr>
<tr class="odd">
<td>5756</td>
<td>TRINITY_DN3374_c0_g2_i1</td>
<td>ko:K19478</td>
</tr>
<tr class="even">
<td>5760</td>
<td>TRINITY_DN8840_c0_g1_i1</td>
<td>ko:K23034</td>
</tr>
<tr class="odd">
<td>5781</td>
<td>TRINITY_DN8262_c0_g1_i1</td>
<td>ko:K18269</td>
</tr>
<tr class="even">
<td>5802</td>
<td>TRINITY_DN7154_c0_g1_i1</td>
<td>ko:K14397</td>
</tr>
<tr class="odd">
<td>5812</td>
<td>TRINITY_DN25826_c0_g1_i1</td>
<td>ko:K22942</td>
</tr>
<tr class="even">
<td>5843</td>
<td>TRINITY_DN6270_c0_g1_i1</td>
<td>ko:K05752</td>
</tr>
<tr class="odd">
<td>5844</td>
<td>TRINITY_DN6270_c0_g2_i1</td>
<td>ko:K05752</td>
</tr>
<tr class="even">
<td>5845</td>
<td>TRINITY_DN23611_c0_g1_i1</td>
<td>ko:K13120</td>
</tr>
<tr class="odd">
<td>5850</td>
<td>TRINITY_DN6335_c0_g1_i1</td>
<td>ko:K07910</td>
</tr>
<tr class="even">
<td>5852</td>
<td>TRINITY_DN6291_c1_g1_i1</td>
<td>ko:K08824</td>
</tr>
<tr class="odd">
<td>5856</td>
<td>TRINITY_DN27292_c0_g1_i1</td>
<td>ko:K03020</td>
</tr>
<tr class="even">
<td>5858</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07880</td>
</tr>
<tr class="odd">
<td>5867</td>
<td>TRINITY_DN5762_c0_g1_i1</td>
<td>ko:K12947</td>
</tr>
<tr class="even">
<td>5868</td>
<td>TRINITY_DN5762_c0_g2_i1</td>
<td>ko:K12947</td>
</tr>
<tr class="odd">
<td>5871</td>
<td>TRINITY_DN6163_c0_g1_i1</td>
<td>ko:K22939</td>
</tr>
<tr class="even">
<td>5875</td>
<td>TRINITY_DN5413_c0_g1_i1</td>
<td>ko:K19695</td>
</tr>
<tr class="odd">
<td>5883</td>
<td>TRINITY_DN9166_c0_g1_i1</td>
<td>ko:K22390</td>
</tr>
<tr class="even">
<td>5884</td>
<td>TRINITY_DN9166_c0_g1_i3</td>
<td>ko:K22390</td>
</tr>
<tr class="odd">
<td>5890</td>
<td>TRINITY_DN9513_c2_g4_i1</td>
<td>ko:K05692</td>
</tr>
<tr class="even">
<td>5894</td>
<td>TRINITY_DN7045_c0_g1_i1</td>
<td>ko:K12581</td>
</tr>
<tr class="odd">
<td>5896</td>
<td>TRINITY_DN6319_c0_g1_i1</td>
<td>ko:K03627</td>
</tr>
<tr class="even">
<td>6035</td>
<td>TRINITY_DN9269_c0_g1_i1</td>
<td>ko:K03233</td>
</tr>
<tr class="odd">
<td>6059</td>
<td>TRINITY_DN9363_c0_g1_i1</td>
<td>ko:K00240</td>
</tr>
<tr class="even">
<td>6066</td>
<td>TRINITY_DN308_c0_g1_i1</td>
<td>ko:K02913</td>
</tr>
<tr class="odd">
<td>6086</td>
<td>TRINITY_DN9340_c0_g1_i1</td>
<td>ko:K01881</td>
</tr>
<tr class="even">
<td>6095</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K09565</td>
</tr>
<tr class="odd">
<td>6173</td>
<td>TRINITY_DN9114_c0_g1_i2</td>
<td>ko:K12753</td>
</tr>
<tr class="even">
<td>6174</td>
<td>TRINITY_DN9114_c0_g1_i1</td>
<td>ko:K12753</td>
</tr>
<tr class="odd">
<td>6175</td>
<td>TRINITY_DN9114_c0_g1_i3</td>
<td>ko:K12753</td>
</tr>
<tr class="even">
<td>6295</td>
<td>TRINITY_DN8941_c0_g1_i1</td>
<td>ko:K07888</td>
</tr>
<tr class="odd">
<td>6342</td>
<td>TRINITY_DN8422_c0_g1_i2</td>
<td>ko:K16790</td>
</tr>
<tr class="even">
<td>6353</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07857</td>
</tr>
<tr class="odd">
<td>6354</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07857</td>
</tr>
<tr class="even">
<td>6355</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07857</td>
</tr>
<tr class="odd">
<td>6356</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07857</td>
</tr>
<tr class="even">
<td>6383</td>
<td>TRINITY_DN9114_c0_g1_i1</td>
<td>ko:K12755</td>
</tr>
<tr class="odd">
<td>6384</td>
<td>TRINITY_DN9114_c0_g1_i3</td>
<td>ko:K12755</td>
</tr>
<tr class="even">
<td>6385</td>
<td>TRINITY_DN9114_c0_g1_i2</td>
<td>ko:K12755</td>
</tr>
<tr class="odd">
<td>6386</td>
<td>TRINITY_DN9024_c0_g1_i1</td>
<td>ko:K12755</td>
</tr>
<tr class="even">
<td>6387</td>
<td>TRINITY_DN6480_c0_g1_i1</td>
<td>ko:K12755</td>
</tr>
<tr class="odd">
<td>6388</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K02833</td>
</tr>
<tr class="even">
<td>6389</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K02833</td>
</tr>
<tr class="odd">
<td>6390</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K02833</td>
</tr>
<tr class="even">
<td>6394</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07940</td>
</tr>
<tr class="odd">
<td>6395</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07940</td>
</tr>
<tr class="even">
<td>6396</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07940</td>
</tr>
<tr class="odd">
<td>6397</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07940</td>
</tr>
<tr class="even">
<td>6398</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07940</td>
</tr>
<tr class="odd">
<td>6399</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07940</td>
</tr>
<tr class="even">
<td>6424</td>
<td>TRINITY_DN9619_c0_g1_i1</td>
<td>ko:K09490</td>
</tr>
<tr class="odd">
<td>6478</td>
<td>TRINITY_DN1721_c0_g1_i1</td>
<td>ko:K07828</td>
</tr>
<tr class="even">
<td>6479</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07828</td>
</tr>
<tr class="odd">
<td>6480</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K07828</td>
</tr>
<tr class="even">
<td>6508</td>
<td>TRINITY_DN8530_c0_g1_i1</td>
<td>ko:K07903</td>
</tr>
<tr class="odd">
<td>6509</td>
<td>TRINITY_DN8731_c0_g1_i1</td>
<td>ko:K07903</td>
</tr>
<tr class="even">
<td>6519</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K12313</td>
</tr>
<tr class="odd">
<td>6524</td>
<td>TRINITY_DN4539_c0_g1_i1</td>
<td>ko:K21751</td>
</tr>
<tr class="even">
<td>6574</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07941</td>
</tr>
<tr class="odd">
<td>6577</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07941</td>
</tr>
<tr class="even">
<td>6605</td>
<td>TRINITY_DN8993_c1_g1_i5</td>
<td>ko:K04551</td>
</tr>
<tr class="odd">
<td>6606</td>
<td>TRINITY_DN8993_c1_g1_i2</td>
<td>ko:K04551</td>
</tr>
<tr class="even">
<td>6608</td>
<td>TRINITY_DN8993_c1_g1_i11</td>
<td>ko:K04551</td>
</tr>
<tr class="odd">
<td>6768</td>
<td>TRINITY_DN5565_c0_g1_i1</td>
<td>ko:K02639</td>
</tr>
<tr class="even">
<td>6810</td>
<td>TRINITY_DN24450_c0_g1_i1</td>
<td>ko:K02078</td>
</tr>
<tr class="odd">
<td>6851</td>
<td>TRINITY_DN6166_c0_g1_i1</td>
<td>ko:K17095</td>
</tr>
<tr class="even">
<td>6928</td>
<td>TRINITY_DN9075_c0_g1_i2</td>
<td>ko:K13182</td>
</tr>
<tr class="odd">
<td>6929</td>
<td>TRINITY_DN9075_c0_g1_i3</td>
<td>ko:K13182</td>
</tr>
<tr class="even">
<td>6949</td>
<td>TRINITY_DN12789_c0_g1_i1</td>
<td>ko:K14568</td>
</tr>
<tr class="odd">
<td>6953</td>
<td>TRINITY_DN20712_c0_g1_i1</td>
<td>ko:K11663</td>
</tr>
<tr class="even">
<td>6985</td>
<td>TRINITY_DN8231_c0_g1_i1</td>
<td>ko:K07876</td>
</tr>
<tr class="odd">
<td>6986</td>
<td>TRINITY_DN8231_c0_g1_i2</td>
<td>ko:K07876</td>
</tr>
<tr class="even">
<td>6987</td>
<td>TRINITY_DN8731_c0_g2_i1</td>
<td>ko:K07876</td>
</tr>
<tr class="odd">
<td>6988</td>
<td>TRINITY_DN2076_c0_g1_i1</td>
<td>ko:K07891</td>
</tr>
<tr class="even">
<td>7007</td>
<td>TRINITY_DN8164_c0_g1_i1</td>
<td>ko:K08870</td>
</tr>
<tr class="odd">
<td>7022</td>
<td>TRINITY_DN5994_c0_g1_i1</td>
<td>ko:K12395</td>
</tr>
<tr class="even">
<td>7023</td>
<td>TRINITY_DN2939_c0_g1_i1</td>
<td>ko:K02267</td>
</tr>
<tr class="odd">
<td>7024</td>
<td>TRINITY_DN3143_c0_g1_i1</td>
<td>ko:K10582</td>
</tr>
<tr class="even">
<td>7025</td>
<td>TRINITY_DN8626_c0_g1_i1</td>
<td>ko:K08795</td>
</tr>
<tr class="odd">
<td>7045</td>
<td>TRINITY_DN9355_c0_g1_i2</td>
<td>ko:K01371</td>
</tr>
<tr class="even">
<td>7046</td>
<td>TRINITY_DN9355_c0_g1_i5</td>
<td>ko:K01371</td>
</tr>
<tr class="odd">
<td>7052</td>
<td>TRINITY_DN9653_c1_g1_i1</td>
<td>ko:K01375</td>
</tr>
<tr class="even">
<td>7053</td>
<td>TRINITY_DN9355_c0_g1_i5</td>
<td>ko:K01375</td>
</tr>
<tr class="odd">
<td>7054</td>
<td>TRINITY_DN9355_c0_g1_i4</td>
<td>ko:K01375</td>
</tr>
<tr class="even">
<td>7055</td>
<td>TRINITY_DN9355_c0_g1_i1</td>
<td>ko:K01375</td>
</tr>
<tr class="odd">
<td>7056</td>
<td>TRINITY_DN9355_c0_g1_i2</td>
<td>ko:K01375</td>
</tr>
<tr class="even">
<td>7100</td>
<td>TRINITY_DN9116_c0_g1_i1</td>
<td>ko:K08549</td>
</tr>
<tr class="odd">
<td>7101</td>
<td>TRINITY_DN9116_c0_g1_i2</td>
<td>ko:K08549</td>
</tr>
<tr class="even">
<td>7114</td>
<td>TRINITY_DN9333_c0_g1_i1</td>
<td>ko:K00129</td>
</tr>
<tr class="odd">
<td>7115</td>
<td>TRINITY_DN6492_c1_g1_i1</td>
<td>ko:K07950</td>
</tr>
<tr class="even">
<td>7124</td>
<td>TRINITY_DN9923_c0_g1_i1</td>
<td>ko:K07831</td>
</tr>
<tr class="odd">
<td>7134</td>
<td>TRINITY_DN11126_c0_g1_i1</td>
<td>ko:K20350</td>
</tr>
<tr class="even">
<td>7135</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07194</td>
</tr>
<tr class="odd">
<td>7136</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07194</td>
</tr>
<tr class="even">
<td>7137</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07194</td>
</tr>
<tr class="odd">
<td>7139</td>
<td>TRINITY_DN8874_c0_g1_i1</td>
<td>ko:K12828</td>
</tr>
<tr class="even">
<td>7141</td>
<td>TRINITY_DN24797_c0_g1_i1</td>
<td>ko:K18646</td>
</tr>
<tr class="odd">
<td>7145</td>
<td>TRINITY_DN8558_c0_g1_i1</td>
<td>ko:K07923</td>
</tr>
<tr class="even">
<td>7146</td>
<td>TRINITY_DN9537_c1_g1_i1</td>
<td>ko:K00547</td>
</tr>
<tr class="odd">
<td>7170</td>
<td>TRINITY_DN8076_c0_g1_i1</td>
<td>ko:K11980</td>
</tr>
<tr class="even">
<td>7173</td>
<td>TRINITY_DN9575_c4_g1_i2</td>
<td>ko:K00552</td>
</tr>
<tr class="odd">
<td>7187</td>
<td>TRINITY_DN9259_c1_g1_i1</td>
<td>ko:K04535</td>
</tr>
<tr class="even">
<td>7188</td>
<td>TRINITY_DN9504_c0_g1_i1</td>
<td>ko:K04537</td>
</tr>
<tr class="odd">
<td>7190</td>
<td>TRINITY_DN7767_c0_g1_i1</td>
<td>ko:K06644</td>
</tr>
<tr class="even">
<td>7191</td>
<td>TRINITY_DN9134_c0_g2_i1</td>
<td>ko:K06644</td>
</tr>
<tr class="odd">
<td>7192</td>
<td>TRINITY_DN8511_c0_g1_i1</td>
<td>ko:K06644</td>
</tr>
<tr class="even">
<td>7193</td>
<td>TRINITY_DN9134_c0_g2_i2</td>
<td>ko:K06644</td>
</tr>
<tr class="odd">
<td>7194</td>
<td>TRINITY_DN9134_c0_g1_i3</td>
<td>ko:K06644</td>
</tr>
<tr class="even">
<td>7195</td>
<td>TRINITY_DN9134_c0_g1_i2</td>
<td>ko:K06644</td>
</tr>
<tr class="odd">
<td>7207</td>
<td>TRINITY_DN8336_c0_g1_i1</td>
<td>ko:K08822</td>
</tr>
<tr class="even">
<td>7255</td>
<td>TRINITY_DN7542_c0_g1_i1</td>
<td>ko:K07896</td>
</tr>
<tr class="odd">
<td>7285</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07863</td>
</tr>
<tr class="even">
<td>7286</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07863</td>
</tr>
<tr class="odd">
<td>7287</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07863</td>
</tr>
<tr class="even">
<td>7288</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07863</td>
</tr>
<tr class="odd">
<td>7300</td>
<td>TRINITY_DN8422_c0_g1_i2</td>
<td>ko:K16791</td>
</tr>
<tr class="even">
<td>7320</td>
<td>TRINITY_DN9114_c0_g1_i1</td>
<td>ko:K10351</td>
</tr>
<tr class="odd">
<td>7321</td>
<td>TRINITY_DN9114_c0_g1_i2</td>
<td>ko:K10351</td>
</tr>
<tr class="even">
<td>7322</td>
<td>TRINITY_DN9114_c0_g1_i3</td>
<td>ko:K10351</td>
</tr>
<tr class="odd">
<td>7374</td>
<td>TRINITY_DN11126_c0_g1_i1</td>
<td>ko:K20349</td>
</tr>
<tr class="even">
<td>7389</td>
<td>TRINITY_DN7542_c0_g1_i1</td>
<td>ko:K07894</td>
</tr>
<tr class="odd">
<td>7426</td>
<td>TRINITY_DN1694_c0_g1_i1</td>
<td>ko:K21891</td>
</tr>
<tr class="even">
<td>7447</td>
<td>TRINITY_DN7235_c0_g1_i1</td>
<td>ko:K11584</td>
</tr>
<tr class="odd">
<td>7476</td>
<td>TRINITY_DN5824_c0_g1_i1</td>
<td>ko:K04431</td>
</tr>
<tr class="even">
<td>7483</td>
<td>TRINITY_DN5721_c0_g1_i1</td>
<td>ko:K02728</td>
</tr>
<tr class="odd">
<td>7485</td>
<td>TRINITY_DN9327_c1_g1_i1</td>
<td>ko:K17087</td>
</tr>
<tr class="even">
<td>7503</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07864</td>
</tr>
<tr class="odd">
<td>7504</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07864</td>
</tr>
<tr class="even">
<td>7505</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07864</td>
</tr>
<tr class="odd">
<td>7506</td>
<td>TRINITY_DN1109_c0_g1_i1</td>
<td>ko:K12621</td>
</tr>
<tr class="even">
<td>7508</td>
<td>TRINITY_DN8431_c0_g1_i1</td>
<td>ko:K16186</td>
</tr>
<tr class="odd">
<td>7509</td>
<td>TRINITY_DN8431_c0_g1_i2</td>
<td>ko:K16186</td>
</tr>
<tr class="even">
<td>7531</td>
<td>TRINITY_DN9378_c0_g1_i1</td>
<td>ko:K07861</td>
</tr>
<tr class="odd">
<td>7532</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07861</td>
</tr>
<tr class="even">
<td>7533</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07861</td>
</tr>
<tr class="odd">
<td>7534</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07861</td>
</tr>
<tr class="even">
<td>7535</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07837</td>
</tr>
<tr class="odd">
<td>7536</td>
<td>TRINITY_DN122_c1_g1_i1</td>
<td>ko:K07837</td>
</tr>
<tr class="even">
<td>7539</td>
<td>TRINITY_DN9504_c0_g1_i1</td>
<td>ko:K04538</td>
</tr>
<tr class="odd">
<td>7585</td>
<td>TRINITY_DN9424_c0_g1_i1</td>
<td>ko:K17254</td>
</tr>
<tr class="even">
<td>7594</td>
<td>TRINITY_DN9266_c1_g2_i1</td>
<td>ko:K12738</td>
</tr>
<tr class="odd">
<td>7595</td>
<td>TRINITY_DN9399_c0_g1_i1</td>
<td>ko:K12738</td>
</tr>
<tr class="even">
<td>7617</td>
<td>TRINITY_DN1698_c0_g2_i1</td>
<td>ko:K03872</td>
</tr>
<tr class="odd">
<td>7618</td>
<td>TRINITY_DN1698_c0_g1_i1</td>
<td>ko:K03872</td>
</tr>
<tr class="even">
<td>7619</td>
<td>TRINITY_DN1698_c0_g3_i1</td>
<td>ko:K03872</td>
</tr>
<tr class="odd">
<td>7620</td>
<td>TRINITY_DN8603_c0_g1_i2</td>
<td>ko:K03873</td>
</tr>
<tr class="even">
<td>7621</td>
<td>TRINITY_DN8603_c0_g1_i1</td>
<td>ko:K03873</td>
</tr>
<tr class="odd">
<td>7629</td>
<td>TRINITY_DN8846_c0_g1_i1</td>
<td>ko:K05764</td>
</tr>
<tr class="even">
<td>7648</td>
<td>TRINITY_DN13804_c0_g1_i1</td>
<td>ko:K10576</td>
</tr>
<tr class="odd">
<td>7659</td>
<td>TRINITY_DN8341_c0_g2_i1</td>
<td>ko:K05862</td>
</tr>
<tr class="even">
<td>7686</td>
<td>TRINITY_DN8884_c0_g2_i4</td>
<td>ko:K15523</td>
</tr>
<tr class="odd">
<td>7687</td>
<td>TRINITY_DN8884_c0_g2_i3</td>
<td>ko:K15523</td>
</tr>
<tr class="even">
<td>7697</td>
<td>TRINITY_DN9068_c0_g1_i1</td>
<td>ko:K09595</td>
</tr>
<tr class="odd">
<td>7768</td>
<td>TRINITY_DN7542_c0_g1_i1</td>
<td>ko:K07895</td>
</tr>
<tr class="even">
<td>7771</td>
<td>TRINITY_DN14357_c0_g1_i1</td>
<td>ko:K10427</td>
</tr>
<tr class="odd">
<td>7774</td>
<td>TRINITY_DN8173_c0_g1_i1</td>
<td>ko:K14965</td>
</tr>
<tr class="even">
<td>7778</td>
<td>TRINITY_DN8931_c0_g1_i1</td>
<td>ko:K09667</td>
</tr>
<tr class="odd">
<td>7785</td>
<td>TRINITY_DN6274_c0_g1_i2</td>
<td>ko:K07878</td>
</tr>
<tr class="even">
<td>7786</td>
<td>TRINITY_DN8016_c0_g1_i1</td>
<td>ko:K07878</td>
</tr>
<tr class="odd">
<td>7787</td>
<td>TRINITY_DN6274_c0_g1_i1</td>
<td>ko:K07878</td>
</tr>
<tr class="even">
<td>7788</td>
<td>TRINITY_DN9437_c0_g2_i2</td>
<td>ko:K18202</td>
</tr>
<tr class="odd">
<td>7807</td>
<td>TRINITY_DN20351_c0_g1_i1</td>
<td>ko:K08508</td>
</tr>
<tr class="even">
<td>7830</td>
<td>TRINITY_DN8278_c0_g1_i1</td>
<td>ko:K04553</td>
</tr>
<tr class="odd">
<td>7840</td>
<td>TRINITY_DN16505_c0_g1_i1</td>
<td>ko:K10611</td>
</tr>
<tr class="even">
<td>7846</td>
<td>TRINITY_DN3336_c0_g1_i1</td>
<td>ko:K02207</td>
</tr>
<tr class="odd">
<td>7847</td>
<td>TRINITY_DN3336_c0_g2_i1</td>
<td>ko:K02207</td>
</tr>
<tr class="even">
<td>7927</td>
<td>TRINITY_DN6066_c0_g1_i1</td>
<td>ko:K02974</td>
</tr>
<tr class="odd">
<td>8491</td>
<td>TRINITY_DN8852_c0_g1_i2</td>
<td>ko:K06689</td>
</tr>
<tr class="even">
<td>8493</td>
<td>TRINITY_DN8852_c0_g1_i1</td>
<td>ko:K06689</td>
</tr>
<tr class="odd">
<td>8508</td>
<td>TRINITY_DN8080_c0_g1_i1</td>
<td>ko:K02437</td>
</tr>
<tr class="even">
<td>8510</td>
<td>TRINITY_DN8391_c0_g1_i1</td>
<td>ko:K02956</td>
</tr>
<tr class="odd">
<td>8526</td>
<td>TRINITY_DN6976_c0_g1_i1</td>
<td>ko:K03058</td>
</tr>
<tr class="even">
<td>8527</td>
<td>TRINITY_DN6976_c0_g2_i1</td>
<td>ko:K03058</td>
</tr>
<tr class="odd">
<td>8750</td>
<td>TRINITY_DN5072_c0_g1_i1</td>
<td>ko:K14455</td>
</tr>
<tr class="even">
<td>8754</td>
<td>TRINITY_DN9094_c0_g1_i1</td>
<td>ko:K08056</td>
</tr>
<tr class="odd">
<td>8918</td>
<td>TRINITY_DN9451_c0_g1_i1</td>
<td>ko:K07898</td>
</tr>
<tr class="even">
<td>9042</td>
<td>TRINITY_DN9451_c0_g1_i1</td>
<td>ko:K07900</td>
</tr>
<tr class="odd">
<td>9137</td>
<td>TRINITY_DN8862_c0_g1_i1</td>
<td>ko:K00799</td>
</tr>
<tr class="even">
<td>9241</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07839</td>
</tr>
<tr class="odd">
<td>9242</td>
<td>TRINITY_DN122_c1_g1_i1</td>
<td>ko:K07839</td>
</tr>
<tr class="even">
<td>9375</td>
<td>TRINITY_DN9320_c0_g2_i2</td>
<td>ko:K02996</td>
</tr>
<tr class="odd">
<td>9664</td>
<td>TRINITY_DN6990_c0_g1_i1</td>
<td>ko:K01802</td>
</tr>
<tr class="even">
<td>9815</td>
<td>TRINITY_DN14997_c0_g1_i1</td>
<td>ko:K01551</td>
</tr>
<tr class="odd">
<td>9816</td>
<td>TRINITY_DN8921_c1_g1_i1</td>
<td>ko:K03250</td>
</tr>
<tr class="even">
<td>9817</td>
<td>TRINITY_DN4236_c0_g2_i1</td>
<td>ko:K13176</td>
</tr>
<tr class="odd">
<td>9818</td>
<td>TRINITY_DN4236_c0_g1_i1</td>
<td>ko:K13176</td>
</tr>
<tr class="even">
<td>9819</td>
<td>TRINITY_DN8464_c0_g1_i1</td>
<td>ko:K03247</td>
</tr>
<tr class="odd">
<td>9823</td>
<td>TRINITY_DN19644_c0_g1_i1</td>
<td>ko:K11884</td>
</tr>
<tr class="even">
<td>9826</td>
<td>TRINITY_DN8217_c0_g2_i2</td>
<td>ko:K16344</td>
</tr>
<tr class="odd">
<td>9827</td>
<td>TRINITY_DN8217_c0_g2_i1</td>
<td>ko:K16344</td>
</tr>
<tr class="even">
<td>9828</td>
<td>TRINITY_DN6229_c0_g1_i1</td>
<td>ko:K20399</td>
</tr>
<tr class="odd">
<td>9829</td>
<td>TRINITY_DN1593_c0_g1_i1</td>
<td>ko:K03251</td>
</tr>
<tr class="even">
<td>9834</td>
<td>TRINITY_DN7213_c0_g1_i1</td>
<td>ko:K16794</td>
</tr>
<tr class="odd">
<td>9971</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K12314</td>
</tr>
<tr class="even">
<td>10363</td>
<td>TRINITY_DN8934_c0_g1_i1</td>
<td>ko:K02965</td>
</tr>
<tr class="odd">
<td>10552</td>
<td>TRINITY_DN15399_c0_g1_i1</td>
<td>ko:K00332</td>
</tr>
<tr class="even">
<td>11082</td>
<td>TRINITY_DN6530_c0_g1_i1</td>
<td>ko:K00334</td>
</tr>
<tr class="odd">
<td>11264</td>
<td>TRINITY_DN1046_c0_g1_i1</td>
<td>ko:K03262</td>
</tr>
<tr class="even">
<td>11287</td>
<td>TRINITY_DN11372_c0_g1_i1</td>
<td>ko:K02151</td>
</tr>
<tr class="odd">
<td>11310</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="even">
<td>11311</td>
<td>TRINITY_DN14400_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="odd">
<td>11312</td>
<td>TRINITY_DN14631_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="even">
<td>11313</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="odd">
<td>11314</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K07938</td>
</tr>
<tr class="even">
<td>11315</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="odd">
<td>11316</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="even">
<td>11317</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K07938</td>
</tr>
<tr class="odd">
<td>11323</td>
<td>TRINITY_DN122_c1_g1_i1</td>
<td>ko:K07838</td>
</tr>
<tr class="even">
<td>11324</td>
<td>TRINITY_DN8440_c0_g2_i1</td>
<td>ko:K07838</td>
</tr>
<tr class="odd">
<td>11327</td>
<td>TRINITY_DN5202_c0_g1_i1</td>
<td>ko:K09398</td>
</tr>
<tr class="even">
<td>11328</td>
<td>TRINITY_DN7380_c0_g1_i1</td>
<td>ko:K09398</td>
</tr>
<tr class="odd">
<td>11394</td>
<td>TRINITY_DN9396_c1_g1_i1</td>
<td>ko:K09455</td>
</tr>
<tr class="even">
<td>11416</td>
<td>TRINITY_DN9513_c2_g1_i1</td>
<td>ko:K12315</td>
</tr>
<tr class="odd">
<td>11732</td>
<td>TRINITY_DN8633_c0_g1_i1</td>
<td>ko:K07856</td>
</tr>
<tr class="even">
<td>11733</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07856</td>
</tr>
<tr class="odd">
<td>11734</td>
<td>TRINITY_DN8633_c0_g1_i2</td>
<td>ko:K07856</td>
</tr>
<tr class="even">
<td>11772</td>
<td>TRINITY_DN8940_c0_g1_i2</td>
<td>ko:K06883</td>
</tr>
<tr class="odd">
<td>11773</td>
<td>TRINITY_DN6858_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="even">
<td>11774</td>
<td>TRINITY_DN9138_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="odd">
<td>11775</td>
<td>TRINITY_DN14400_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="even">
<td>11776</td>
<td>TRINITY_DN6858_c0_g2_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="odd">
<td>11777</td>
<td>TRINITY_DN8426_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="even">
<td>11778</td>
<td>TRINITY_DN8940_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="odd">
<td>11779</td>
<td>TRINITY_DN14631_c0_g1_i1</td>
<td>ko:K06883</td>
</tr>
<tr class="even">
<td>12231</td>
<td>TRINITY_DN17630_c0_g1_i1</td>
<td>ko:K02901</td>
</tr>
<tr class="odd">
<td>12417</td>
<td>TRINITY_DN8545_c0_g1_i1</td>
<td>ko:K07975</td>
</tr>
<tr class="even">
<td>12712</td>
<td>TRINITY_DN9578_c0_g1_i1</td>
<td>ko:K00643</td>
</tr>
<tr class="odd">
<td>12833</td>
<td>TRINITY_DN1045_c0_g1_i1</td>
<td>ko:K10580</td>
</tr>
<tr class="even">
<td>13004</td>
<td>TRINITY_DN6396_c0_g1_i1</td>
<td>ko:K11495</td>
</tr>
<tr class="odd">
<td>13005</td>
<td>TRINITY_DN28548_c0_g1_i1</td>
<td>ko:K11495</td>
</tr>
<tr class="even">
<td>13098</td>
<td>TRINITY_DN9360_c0_g1_i1</td>
<td>ko:K14758</td>
</tr>
<tr class="odd">
<td>13120</td>
<td>TRINITY_DN4830_c0_g1_i1</td>
<td>ko:K11827</td>
</tr>
<tr class="even">
<td>13237</td>
<td>TRINITY_DN9344_c0_g1_i2</td>
<td>ko:K05759</td>
</tr>
<tr class="odd">
<td>13238</td>
<td>TRINITY_DN9344_c0_g1_i3</td>
<td>ko:K05759</td>
</tr>
<tr class="even">
<td>13239</td>
<td>TRINITY_DN9344_c0_g1_i1</td>
<td>ko:K05759</td>
</tr>
<tr class="odd">
<td>13279</td>
<td>TRINITY_DN9644_c0_g1_i2</td>
<td>ko:K00933</td>
</tr>
<tr class="even">
<td>13281</td>
<td>TRINITY_DN15607_c0_g1_i1</td>
<td>ko:K00933</td>
</tr>
<tr class="odd">
<td>13318</td>
<td>TRINITY_DN7265_c0_g1_i1</td>
<td>ko:K06704</td>
</tr>
<tr class="even">
<td>13748</td>
<td>TRINITY_DN25525_c0_g1_i1</td>
<td>ko:K22069</td>
</tr>
<tr class="odd">
<td>14202</td>
<td>TRINITY_DN9408_c0_g1_i1</td>
<td>ko:K00522</td>
</tr>
<tr class="even">
<td>14314</td>
<td>TRINITY_DN14400_c0_g1_i1</td>
<td>ko:K07939</td>
</tr>
<tr class="odd">
<td>14332</td>
<td>TRINITY_DN7550_c1_g1_i1</td>
<td>ko:K04505</td>
</tr>
<tr class="even">
<td>14333</td>
<td>TRINITY_DN7550_c1_g2_i1</td>
<td>ko:K04505</td>
</tr>
</tbody>
</table>
