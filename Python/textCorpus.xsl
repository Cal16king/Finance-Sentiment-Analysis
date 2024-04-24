<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="text"/>


    <!-- declare variable $results := doc('results.xml');
    
    
    let $keys := $results//key
    for $k in $keys
    let $date := $k/date
    let $art := $k/@name ! string()
    return   
    
    --> 
  <xsl:variable name="results" as="document-node()" select="doc('results.xml')"/>
        
        
      <xsl:template match="/">
          
          <xsl:apply-templates select="//key"/>
            
      </xsl:template>
    
    <xsl:template match="key">
        <xsl:variable name="filename" as="xs:string" select="@name ! substring(., 1, 20) ! replace(., '\W', '') ! lower-case(.)"/>
     
        <xsl:value-of select="$filename"/>
        <xsl:result-document method="text" href="textCorpus/{date}-{$filename}.txt">
            
            <xsl:value-of select="@name"/>
            
            
        </xsl:result-document>
        
        
    </xsl:template>

    
    
    
    
</xsl:stylesheet>