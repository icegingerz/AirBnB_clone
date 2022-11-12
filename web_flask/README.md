# 0x04. AirBnB clone - Web framework

### Task 0
- Files ( 0-hello_route.py init.py)
<!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &quot;Hello HBNB!&quot;</li>
<li><code>/hbnb</code>: display &quot;HBNB&quot;</li>
<li><code>/c/&lt;text&gt;</code>: display &quot;C &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &quot;Python &quot;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &quot;is cool&quot;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &quot;<code>n</code> is a number&quot; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &quot;Number: <code>n</code>&quot; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &quot;Number: <code>n</code> is <code>even|odd</code>&quot; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>
